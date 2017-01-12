from __future__ import print_function
import sys
import random

class ScreenRes(object):
    @classmethod
    def set(cls, width=None, height=None, depth=32):
        '''
        Set the primary display to the specified mode
        '''
        if width and height:
            print('Setting resolution to {}x{}'.format(width, height, depth))
        else:
            print('Setting resolution to defaults')

        if sys.platform == 'win32':
            cls._win32_set(width, height, depth)
        elif sys.platform.startswith('linux'):
            cls._linux_set(width, height, depth)
        elif sys.platform.startswith('darwin'):
            cls._osx_set(width, height, depth)

    @classmethod
    def get(cls):
        if sys.platform == 'win32':
            return cls._win32_get()
        elif sys.platform.startswith('linux'):
            return cls._linux_get()
        elif sys.platform.startswith('darwin'):
            return cls._osx_get()

    @classmethod
    def get_modes(cls):
        if sys.platform == 'win32':
            return cls._win32_get_modes()
        elif sys.platform.startswith('linux'):
            return cls._linux_get_modes()
        elif sys.platform.startswith('darwin'):
            return cls._osx_get_modes()

    @staticmethod
    def _win32_get_modes():
        '''
        Get the primary windows display width and height
        '''
        import win32api
        from pywintypes import DEVMODEType, error
        modes = []
        i = 0
        try:
            while True:
                mode = win32api.EnumDisplaySettings(None, i)
                modes.append((
                    int(mode.PelsWidth),
                    int(mode.PelsHeight),
                    int(mode.BitsPerPel),
                    ))
                i += 1
        except error:
            pass

        return modes

    @staticmethod
    def _win32_get():
        '''
        Get the primary windows display width and height
        '''
        import ctypes
        user32 = ctypes.windll.user32
        screensize = (
            user32.GetSystemMetrics(0), 
            user32.GetSystemMetrics(1),
            )
        return screensize

    @staticmethod
    def _win32_set(width=None, height=None, depth=32):
        '''
        Set the primary windows display to the specified mode
        '''
        # Gave up on ctypes, the struct is really complicated
        #user32.ChangeDisplaySettingsW(None, 0)
        import win32api
        from pywintypes import DEVMODEType
        if width and height:

            if not depth:
                depth = 32

            mode = win32api.EnumDisplaySettings()
            mode.PelsWidth = width
            mode.PelsHeight = height
            mode.BitsPerPel = depth

            win32api.ChangeDisplaySettings(mode, 0)
        else:
            win32api.ChangeDisplaySettings(None, 0)


    @staticmethod
    def _win32_set_default():
        '''
        Reset the primary windows display to the default mode
        '''
        # Interesting since it doesn't depend on pywin32
        import ctypes
        user32 = ctypes.windll.user32
        # set screen size
        user32.ChangeDisplaySettingsW(None, 0)

    @staticmethod
    def _linux_set(width=None, height=None, depth=32):
        raise NotImplementedError()

    @staticmethod
    def _linux_get():
        raise NotImplementedError()

    @staticmethod
    def _linux_get_modes():
        raise NotImplementedError()

    @staticmethod
    def _osx_set(width=None, height=None, depth=32):
        raise NotImplementedError()

    @staticmethod
    def _osx_get():
        raise NotImplementedError()

    @staticmethod
    def _osx_get_modes():
        raise NotImplementedError()


def changeScr():
    print('Primary screen resolution: {}x{}'.format(
        *ScreenRes.get()
        ))
    list_screen = random.randint(1,6)
    if list_screen == 1:
        ScreenRes.set(1600,900)
        return "Set resolution: 1600,900"
    elif list_screen == 2:
        ScreenRes.set(800,600)
        return "Set resolution: 800,600"
    elif list_screen == 3:
        ScreenRes.set(1024,768)
        return "Set resolution: 1024,768"
    elif list_screen == 4:
        ScreenRes.set(1280,1024)
        return "Set resolution: 1280,1024"
    elif list_screen == 5:
        ScreenRes.set(1280,768)
        return "Set resolution: 1280,768"
    return "Not set"

    # for i in range(0,lst.__len__()):
    # print(lst[0])
    # ScreenRes.set(1600,900)
    #ScreenRes.set() # Set defaults
