from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectFrame import DirectFrame
from panda3d.core import TransparencyAttrib

class Main(ShowBase):
    def __init__(self):
        super().__init__()

        self.carHitbox = DirectButton(
            parent=self.aspect2d,
            scale=1,
            pos=(0, 0, 0),
            frameColor=(0, 0, 0, 0),
            relief=None
        )

        self.carImg = DirectFrame(
            parent=self.carHitbox,
            image="img/topCar.png",
            scale=(0.23, 1, 0.13),
            frameColor=(0, 0, 0, 0),
            relief=None
        )

        self.road = DirectFrame(
            parent=self.a2dBackground,
            image="img/road.png",
            scale=1,
        )
        self.carHitbox.setHpr(0, 0, 90)
        self.carImg.setTransparency(TransparencyAttrib.MAlpha)

main = Main()
main.run()
