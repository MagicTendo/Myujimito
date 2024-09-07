from os import path
from sys import executable
from webbrowser import open_new
import subprocess

import resource_manager


def change_language(language):
    """
    Update the language in the config.csv
    """
    resource_manager.dataframe.at[resource_manager.dataframe.index[0], "language"] = language
    resource_manager.dataframe.to_csv(resource_manager.get_config(), sep=";", index=False)


def set_boot_up_config():
    """
    Toggle between activating or disactivating the option that allow the application to launch at the boot up of the
    computer, and update it the config.csv and create or delete the task
    """
    user_boot_up = resource_manager.dataframe["boot_up"].values[0]

    if user_boot_up:
        resource_manager.dataframe.at[resource_manager.dataframe.index[0], "boot_up"] = False
        delete_task("Myujimito")
    else:
        resource_manager.dataframe.at[resource_manager.dataframe.index[0], "boot_up"] = True
        create_task("Myujimito")

    resource_manager.dataframe.to_csv(resource_manager.get_config(), sep=";", index=False)


def create_task(task_name):
    """
    Create a task in the Task Manager using a Powershell command to allow the application to automatically launch at the
    computer's boot up
    :param task_name: name of the task, in this case, the name of the application
    """
    command = f"""
        $Trigger = New-ScheduledTaskTrigger -AtStartup;
        $Action = New-ScheduledTaskAction -Execute '{path.realpath(executable)}';
        $Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries:$true -DontStopIfGoingOnBatteries:$true -ExecutionTimeLimit (New-TimeSpan -Hours 0);
        Register-ScheduledTask -Action $Action -Trigger $Trigger -Settings $Settings -TaskName '{task_name}' -Description 'Check if the volume threshold is respected' -User 'SYSTEM' -RunLevel Highest -Force;
    """

    try:
        subprocess.run(["powershell", "-Command", command], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the task\n{e}")


def delete_task(task_name):
    """
    Remove the task to stop the application from launching at the computer's boot up
    :param task_name: name of the task, in this case, the name of the application
    """
    command = ["schtasks", "/delete", "/tn", task_name, "/f"]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while deleting the task\n{e}")


def open_website():
    """
    Open the Myujimito's web page
    """
    open_new("https://bakataida.rf.gd/myujimito")


def open_server_support():
    """
    Open the Yunranohi's Discord server link
    """
    open_new("https://discord.gg/DYQutQvbSu")
