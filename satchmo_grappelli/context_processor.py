from django.conf import settings


def satchmo_grappelli_conf(request):
    use_filebrowser = False

    if 'filebrowser' in settings.INSTALLED_APPS:
        use_filebrowser = True


    return {
        'satchmo_grappelli_use_filebrowser': use_filebrowser
    }