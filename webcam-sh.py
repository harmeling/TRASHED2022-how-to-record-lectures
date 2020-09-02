import sys
import cv2
from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):

    def update_size(self):
        self.width  = round(self.crop[2] * self.scale)
        self.height = round(self.crop[3] * self.scale)
        if self.rotation in [1,3]:
            self.width, self.height = self.height, self.width
        self.root.geometry("{:d}x{:d}".format(self.width, self.height))
        
    def rotate(self, event):
        self.rotation += 1
        if self.rotation == 4:
            self.rotation = 0
        self.update_size()
        
    def increase_window_size(self, event):
        self.scale *= 11/10
        self.update_size()
        
    def decrease_window_size(self, event):
        self.scale *= 10/11
        self.update_size()

    def bye(self, event):
        self.commandline()
        print('BYE')
        self.root.quit()

    def info(self, event):
        print('PARAMETERS')
        print('size     ', self.width, self.height)
        print('position ', self.root.winfo_x(), self.root.winfo_y())
        print('scale    ', self.scale)
        print('crop     ', self.crop)
        print('gray     ', self.gray)
        print('vflip    ', self.vflip)
        print('hflip    ', self.hflip)
        print('rotation ', self.rotation)
        self.commandline()

    def commandline(self):
        print('COMMANDLINE')
        msg = 'python ' + sys.argv[0] \
              + ' -p %d %d' % (self.root.winfo_x(), self.root.winfo_y()) \
              + ' -s %f'    % self.scale
        if self.crop is not None:
            msg += ' -c %d %d %d %d' % (self.crop[0], self.crop[1], self.crop[2], self.crop[3])
        if self.gray:
            msg += ' -g'
        if self.vflip:
            msg += ' -v'
        if self.hflip:
            msg += ' -h'
        if self.rotation != 0:
            msg += ' -r %d' % self.rotation
        print(msg)

    def help(self, event):
        print('KEYS')
        print('g == toggle gray')
        print('h == horizontal flip')
        print('v == vertical flip')
        print('r == rotate')
        print('i == info')
        print('? == help (this message)')
        print('= == increase')
        print('- == decrease')
        print('q == quit')
        
    def toggle_hflip(self, event): self.hflip = not self.hflip
    def toggle_vflip(self, event): self.vflip = not self.vflip
    def toggle_gray (self, event): self.gray  = not self.gray

    def __init__(self, params):
        self.root = Tk()
        Frame.__init__(self, self.root)

        # get a video frame to set initial sizes
        self.cap = cv2.VideoCapture(params['camera'])
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")
        ret, frame  = self.cap.read()
        self.frame_width = frame.shape[1]         # true frame width
        self.frame_height = frame.shape[0]

        # deal with the commandline parameters
        self.hflip    = params['hflip']
        self.vflip    = params['vflip']
        self.gray     = params['gray']
        self.rotation = params['rotation'] or 0
        self.crop     = params['crop']     or [0, 0, frame.shape[1], frame.shape[0]]
        self.position = params['position'] or [10, 10]
        self.posx     = self.position[0]                     # window position
        self.posy     = self.position[1]
        self.scale    = params['scale']    or 0.25
        self.width    = round(self.crop[2] * self.scale)     # the actual size of the window and picture shown
        self.height   = round(self.crop[3] * self.scale)
        if self.rotation in [1,3]:
            self.width, self.height = self.height, self.width

        self.root.wm_title("")
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, self.posx, self.posy))
        self.root.resizable(False, False)
        self.root.wm_attributes("-topmost", True)
        #self.root.wm_attributes("-transparent", True) # ALPHASTUFF
        #self.root.config(bg='systemTransparent')      # ALPHASTUFF

        self.root.bind('h', self.toggle_hflip)
        self.root.bind('v', self.toggle_vflip)
        self.root.bind('g', self.toggle_gray)
        self.root.bind('=', self.increase_window_size)
        self.root.bind('-', self.decrease_window_size)
        self.root.bind('r', self.rotate)
        self.root.bind('i', self.info)
        self.root.bind('?', self.help)
        self.root.bind('q', self.bye)
        self.pack(anchor=NW, fill=BOTH, expand=True)
        
        self.canvas = Canvas(self.root, width = self.frame_width, height = self.frame_height, highlightthickness=0, bd=0)
        #self.canvas.config(bg='systemTransparent')       # ALPHASTUFF
        self.canvas.pack(anchor=NW, fill=BOTH, expand=True)

        self.update()
        self.root.mainloop()

    def update(self):
        self.render = self.get_frame()   # must be stored in the object as well!
        self.canvas.create_image(0, 0, image = self.render, anchor = NW)
        self.root.after(15, self.update)

    def get_frame(self):
        ret, frame = self.cap.read()
        [left, top, width, height] = self.crop
        frame = frame[top:(top+height), left:(left+width)]
        if self.rotation != 0:
            frame = cv2.rotate(frame, self.rotation-1)
            self.update_size()
        frame = cv2.resize(frame, (self.width, self.height), interpolation=cv2.INTER_AREA)
        if self.hflip:
            frame = cv2.flip(frame, 1)
        if self.vflip:
            frame = cv2.flip(frame, 0)
        frame = frame[:,:,-1:-4:-1]       # resorder color channels
        if self.gray:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = Image.fromarray(frame)
        #alpha = Image.new('L', img.size, 100)
        #img.putalpha(alpha)
        return ImageTk.PhotoImage(img)

def parse_args(argv, verbose=True):
    help_msg = "usage: python " + argv[0] + "\n"                \
         + " [-p left top]                 # position\n"        \
         + " [-s scale]                    # scale\n"           \
         + " [-c left top width height]    # crop\n"            \
         + " [-g]                          # gray\n"            \
         + " [-v]                          # vertical flip\n"   \
         + " [-h]                          # horizontal flip\n" \
         + " [-r rotation]                 # rotation\n"        \
         + " [--camera c]                  # camera\n"          \
         + " [--help]                      # usage\n"
    params = {'position' : None,
              'scale'    : None,
              'crop'     : None,
              'rotation' : 0,
              'camera'   : 0,
              'gray'     : False,
              'vflip'    : False,
              'hflip'    : False}
    try:  # to deal with the commandline arguments
        i = 1
        while i < len(argv):
            if argv[i] == '--help':
                raise()
            elif argv[i] == '-g':
                params['gray'] = True
                i += 1
            elif argv[i] == '-h':
                params['hflip'] = True
                i += 1
            elif argv[i] == '-v':
                params['vflip'] = True
                i += 1
            elif argv[i] == '-p':
                params['position'] = (int(argv[i+1]), int(argv[i+2]))
                i += 3
            elif argv[i] == '-s':
                params['scale'] = float(argv[i+1])
                i += 2
            elif argv[i] == '-r':
                params['rotation'] = int(argv[i+1])
                i += 2
            elif argv[i] == '-c':
                params['crop'] = (int(argv[i+1]), int(argv[i+2]), int(argv[i+3]), int(argv[i+4]))
                i += 5
            elif argv[i] == '--camera':
                params['camera'] = int(argv[i+1])
                i += 2
            else:
                print(argv[0] + ": illegal option " + argv[i])
                raise()
    except:
        print(help_msg)
        exit()
    return params


# commandline args
params = parse_args(sys.argv)
app = Window(params)

