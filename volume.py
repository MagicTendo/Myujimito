from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from time import sleep

import resource_manager

run_volume_check = False

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


def check_volume():
    """
    Run only in background, check if the user's volume is higher of the volume threshold, if it is, lower it to the
    user's volume threshold
    """
    run_volume_check = True

    while run_volume_check:
        current_volume = volume.GetMasterVolumeLevelScalar() * 100
        get_volume_threshold = resource_manager.dataframe["volume_threshold"].values[0]

        if int(current_volume) > int(get_volume_threshold):
            volume.SetMasterVolumeLevelScalar(int(get_volume_threshold) / 100, None)

        sleep(0.25)
