import resource_manager


def get_user_language():
    """
    Only give the current language set by the user
    """
    return resource_manager.dataframe["language"].values[0]


# Translations may not be exactly correct
texts = {
    "fr": {
        "myujimito": "Myujimito",
        "current_threshold": "Votre limite sonore est configurée à {threshold}%",
        "new_threshold": "Votre limite sonore est maintenant configurée à {threshold}%",
        "close_message": "Voulez-vous vraiment fermer l'application ? L'application ne sera pas en arrière plan.",
        "close": "Fermer",
        "show": "Afficher",
        "subtitle": "L'application ne fonctionne uniquement en arrière plan !",
        "set": "Appliquer",
        "settings": "Paramètres",
        "set_volume_limit": "Appliquer la limite de volume",
        "run_in_background": "Mettre en arrière plan",
        "change_language": "Changer la langue",
        "open_at_boot_up": "Ouvrir lors du démarrage",
        "server_support": "Rejoindre le serveur Discord de support",
        "help": "Aide"
    },
    "en": {
        "myujimito": "Myujimito",
        "current_threshold": "Your current volume threshold is at {threshold}%",
        "new_threshold": "Your current volume threshold is now at {threshold}%",
        "close_message": "Do you really want to close ? The application will not run in background.",
        "close": "Close",
        "show": "Show",
        "subtitle": "This application works only when it runs in background !",
        "set": "Set",
        "settings": "Settings",
        "set_volume_limit": "Set volume limit",
        "run_in_background": "Run in background",
        "change_language": "Change language",
        "open_at_boot_up": "Open at boot up",
        "server_support": "Join the Discord server support",
        "help": "Help"
    },
    "es": {
        "myujimito": "Myujimito",
        "current_threshold": "Su actual volumen umbral es de {threshold}%",
        "new_threshold": "Su actual volumen umbral es de {threshold}% ahora",
        "close_message": "¿ Quiere cerrar lo ? Esta aplicación no estará en fondo.",
        "close": "Cerrar",
        "show": "Mostrar",
        "subtitle": "¡ Esta aplicación funciona únicamente cuando en fondo !",
        "set": "Aplicar",
        "settings": "Parámetros",
        "set_volume_limit": "Aplicar el volumen umbral",
        "run_in_background": "Ejecutar en fondo",
        "change_language": "Cambiar la idioma",
        "open_at_boot_up": "Abierto a iniciar",
        "server_support": "Unirse al servidor de apoyo Discord",
        "help": "Ayuda"
    },
    "yu": {
        "myujimito": "Myujimito",
        "current_threshold": "Tsutobi ñi miyeno di mea {threshold}％ dei ñujo.",
        "new_threshold": "Dotsi, tsutobi ñi miyeno di mea {threshold}％ dei ñujo.",
        "close_message": "Apurice dei fuderomea ? Apurice na bacugon dei ranošoe.",
        "close": "Fudero",
        "show": "Ameyo",
        "subtitle": "Apurice na bacugon ñi tsadoyi dei funco !",
        "set": "Dinbo",
        "settings": "Ñišendi",
        "set_volume_limit": "Tsutobi ñi miyeno dei dinbo",
        "run_in_background": "Bacugon dei ranoyoe",
        "change_language": "Yunomi dei pajido",
        "open_at_boot_up": "Batapu daz opanu",
        "server_support": "Saba ñi seyan di Discord dei cedano",
        "help": "Seyan"
    },
    "jp": {
        "myujimito": "ミュジミト",
        "current_threshold": "ご現在の音量の閾値は{threshold}％です。",
        "new_threshold": "今、ご現在の音量の閾値は{threshold}％です。",
        "close_message": "本当に閉めますか？このアプリケーションはバックグランドを動かない。",
        "close": "閉める",
        "show": "見せる",
        "subtitle": "このアプリケーションはバックグランドだけ動くよ。",
        "set": "入れる",
        "settings": "設定",
        "set_volume_limit": "音量の閾値を入れる",
        "run_in_background": "バックグランドを動く",
        "change_language": "言語",
        "open_at_boot_up": "起動の間を開く",
        "server_support": "ディスコードの支援のサーバを付ける",
        "help": "助け"
    }
}
