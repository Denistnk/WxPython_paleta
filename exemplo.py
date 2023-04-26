import wx
import numpy

def cores_aleatorias():
    color = list(numpy.random.choice(range(256), size=3))
    return color

pincel = 'white'
class PaletadeCores(wx.Frame):
    def __init__(self, parent, id):
        
        wx.Frame.__init__(self, parent, id, 'Paleta de Cores',size=(600, 850))
        self.painelPrincipal = wx.Panel(self, -1)
        
        #Botões e labels
        self.btGerar = wx.Button(self.painelPrincipal, -1, "Gerar", pos=(190, 15),size=(98,35))
        self.btResetar = wx.Button(self.painelPrincipal, -1,"Resetar", pos=(300,15),size=(98,35))
        self.lbTamanho = wx.StaticText(self.painelPrincipal, -1,"Tamanho", pos=(115,95),size=(98,35))
        self.edTamanho = wx.TextCtrl(self.painelPrincipal,-1, '', pos=(190, 80))
        self.edTamanho.SetBackgroundColour(('white'))
        self.edTamanho.SetForegroundColour(wx.BLACK)
        self.btRedefinir = wx.Button(self.painelPrincipal, -1,"Redefinir", pos=(300,80),size=(98,35))

        #Paletas
        self.fundo1 = wx.Button(self.painelPrincipal, -1, "", pos=(78, 148), size=(104,74))
        self.fundo1.SetBackgroundColour(('red'))
        self.fundo1.Hide()
        self.paleta1 = wx.Button(self.painelPrincipal, -1, "", pos=(80, 150), size=(100,70))

        self.fundo2 = wx.Button(self.painelPrincipal, -1, "", pos=(188, 148), size=(104,74))
        self.fundo2.SetBackgroundColour(('red'))
        self.fundo2.Hide()
        self.paleta2 = wx.Button(self.painelPrincipal, -1, "", pos=(190, 150), size=(100,70))

        self.fundo3 = wx.Button(self.painelPrincipal, -1, "", pos=(298, 148), size=(104,74))
        self.fundo3.SetBackgroundColour(('red'))
        self.fundo3.Hide()
        self.paleta3 = wx.Button(self.painelPrincipal, -1, "", pos=(300, 150), size=(100,70))

        self.fundo4 = wx.Button(self.painelPrincipal, -1, "", pos=(408, 148), size=(104,74))
        self.fundo4.SetBackgroundColour(('red'))
        self.fundo4.Hide()
        self.paleta4 = wx.Button(self.painelPrincipal, -1, "", pos=(410, 150), size=(100,70))

        #Quadro
        self.quadro1 = wx.Button(self.painelPrincipal, -1, "", pos=(30, 250), size=(100,100))
        self.quadro2 = wx.Button(self.painelPrincipal, -1, "", pos=(140, 250), size=(100,100))
        self.quadro3 = wx.Button(self.painelPrincipal, -1, "", pos=(250, 250), size=(100,100))
        self.quadro4 = wx.Button(self.painelPrincipal, -1, "", pos=(360, 250), size=(100,100))
        self.quadro5 = wx.Button(self.painelPrincipal, -1, "", pos=(470, 250), size=(100,100))

        self.quadro6 = wx.Button(self.painelPrincipal, -1, "", pos=(30, 360), size=(100,100))
        self.quadro7 = wx.Button(self.painelPrincipal, -1, "", pos=(140, 360), size=(100,100))
        self.quadro8 = wx.Button(self.painelPrincipal, -1, "", pos=(250, 360), size=(100,100))
        self.quadro9 = wx.Button(self.painelPrincipal, -1, "", pos=(360, 360), size=(100,100))
        self.quadro10 = wx.Button(self.painelPrincipal, -1, "", pos=(470, 360), size=(100,100))

        self.quadro11 = wx.Button(self.painelPrincipal, -1, "", pos=(30, 470), size=(100,100))
        self.quadro12 = wx.Button(self.painelPrincipal, -1, "", pos=(140, 470), size=(100,100))
        self.quadro13 = wx.Button(self.painelPrincipal, -1, "", pos=(250, 470), size=(100,100))
        self.quadro14 = wx.Button(self.painelPrincipal, -1, "", pos=(360, 470), size=(100,100))
        self.quadro15 = wx.Button(self.painelPrincipal, -1, "", pos=(470, 470), size=(100,100))

        self.quadro16 = wx.Button(self.painelPrincipal, -1, "", pos=(30, 580), size=(100,100))
        self.quadro17 = wx.Button(self.painelPrincipal, -1, "", pos=(140, 580), size=(100,100))
        self.quadro18 = wx.Button(self.painelPrincipal, -1, "", pos=(250, 580), size=(100,100))
        self.quadro19 = wx.Button(self.painelPrincipal, -1, "", pos=(360, 580), size=(100,100))
        self.quadro20 = wx.Button(self.painelPrincipal, -1, "", pos=(470, 580), size=(100,100))

        self.quadro21 = wx.Button(self.painelPrincipal, -1, "", pos=(30, 690), size=(100,100))
        self.quadro22 = wx.Button(self.painelPrincipal, -1, "", pos=(140, 690), size=(100,100))
        self.quadro23 = wx.Button(self.painelPrincipal, -1, "", pos=(250, 690), size=(100,100))
        self.quadro24 = wx.Button(self.painelPrincipal, -1, "", pos=(360, 690), size=(100,100))
        self.quadro25 = wx.Button(self.painelPrincipal, -1, "", pos=(470, 690), size=(100,100))

        #Setando backgroundcolour
        self.paleta1.SetBackgroundColour((255,255,255))
        self.paleta2.SetBackgroundColour((255,255,255))
        self.paleta3.SetBackgroundColour((255,255,255))
        self.paleta4.SetBackgroundColour((255,255,255))
        self.quadro1.SetBackgroundColour((255,255,255))
        self.quadro2.SetBackgroundColour((255,255,255))
        self.quadro3.SetBackgroundColour((255,255,255))
        self.quadro4.SetBackgroundColour((255,255,255))
        self.quadro5.SetBackgroundColour((255,255,255))
        self.quadro6.SetBackgroundColour((255,255,255))
        self.quadro7.SetBackgroundColour((255,255,255))
        self.quadro8.SetBackgroundColour((255,255,255))
        self.quadro9.SetBackgroundColour((255,255,255))
        self.quadro10.SetBackgroundColour((255,255,255))
        self.quadro11.SetBackgroundColour((255,255,255))
        self.quadro12.SetBackgroundColour((255,255,255))
        self.quadro13.SetBackgroundColour((255,255,255))
        self.quadro14.SetBackgroundColour((255,255,255))
        self.quadro15.SetBackgroundColour((255,255,255))
        self.quadro16.SetBackgroundColour((255,255,255))
        self.quadro17.SetBackgroundColour((255,255,255))
        self.quadro18.SetBackgroundColour((255,255,255))
        self.quadro19.SetBackgroundColour((255,255,255))
        self.quadro20.SetBackgroundColour((255,255,255))
        self.quadro21.SetBackgroundColour((255,255,255))
        self.quadro22.SetBackgroundColour((255,255,255))
        self.quadro23.SetBackgroundColour((255,255,255))
        self.quadro24.SetBackgroundColour((255,255,255))
        self.quadro25.SetBackgroundColour((255,255,255))

        #Eventos dos botões
        self.Bind(wx.EVT_BUTTON, self.gerar_cores, self.btGerar)
        self.Bind(wx.EVT_BUTTON, self.resetar, self.btResetar)
        self.Bind(wx.EVT_BUTTON, self.redefinir, self.btRedefinir)
        self.Bind(wx.EVT_BUTTON, self.selecao1, self.paleta1)
        self.Bind(wx.EVT_BUTTON, self.selecao2, self.paleta2)
        self.Bind(wx.EVT_BUTTON, self.selecao3, self.paleta3)
        self.Bind(wx.EVT_BUTTON, self.selecao4, self.paleta4)
        self.Bind(wx.EVT_BUTTON, self.pintar1, self.quadro1)
        self.Bind(wx.EVT_BUTTON, self.pintar2, self.quadro2)
        self.Bind(wx.EVT_BUTTON, self.pintar3, self.quadro3)
        self.Bind(wx.EVT_BUTTON, self.pintar4, self.quadro4)
        self.Bind(wx.EVT_BUTTON, self.pintar5, self.quadro5)
        self.Bind(wx.EVT_BUTTON, self.pintar6, self.quadro6)
        self.Bind(wx.EVT_BUTTON, self.pintar7, self.quadro7)
        self.Bind(wx.EVT_BUTTON, self.pintar8, self.quadro8)
        self.Bind(wx.EVT_BUTTON, self.pintar9, self.quadro9)
        self.Bind(wx.EVT_BUTTON, self.pintar10, self.quadro10)
        self.Bind(wx.EVT_BUTTON, self.pintar11, self.quadro11)
        self.Bind(wx.EVT_BUTTON, self.pintar12, self.quadro12)
        self.Bind(wx.EVT_BUTTON, self.pintar13, self.quadro13)
        self.Bind(wx.EVT_BUTTON, self.pintar14, self.quadro14)
        self.Bind(wx.EVT_BUTTON, self.pintar15, self.quadro15)
        self.Bind(wx.EVT_BUTTON, self.pintar16, self.quadro16)
        self.Bind(wx.EVT_BUTTON, self.pintar17, self.quadro17)
        self.Bind(wx.EVT_BUTTON, self.pintar18, self.quadro18)
        self.Bind(wx.EVT_BUTTON, self.pintar19, self.quadro19)
        self.Bind(wx.EVT_BUTTON, self.pintar20, self.quadro20)
        self.Bind(wx.EVT_BUTTON, self.pintar21, self.quadro21)
        self.Bind(wx.EVT_BUTTON, self.pintar22, self.quadro22)
        self.Bind(wx.EVT_BUTTON, self.pintar23, self.quadro23)
        self.Bind(wx.EVT_BUTTON, self.pintar24, self.quadro24)
        self.Bind(wx.EVT_BUTTON, self.pintar25, self.quadro25)

    def gerar_cores(self, event):
        global pincel
        pincel = 'white'
        self.fundo1.Hide()
        self.fundo2.Hide()
        self.fundo3.Hide()
        self.fundo4.Hide()
        self.paleta1.SetBackgroundColour((0,0,0))
        self.paleta2.SetBackgroundColour(cores_aleatorias())
        self.paleta3.SetBackgroundColour(cores_aleatorias())
        self.paleta4.SetBackgroundColour(cores_aleatorias())
        self.painelPrincipal.Refresh()

    def selecao1(self,event):
        global pincel
        if not self.paleta1.BackgroundColour == 'white':
            self.fundo1.Show()
            pincel = self.paleta1.BackgroundColour
            self.fundo2.Hide()
            self.fundo3.Hide()
            self.fundo4.Hide()

    def selecao2(self,event):
        global pincel
        if not self.paleta1.BackgroundColour == 'white':
            self.fundo2.Show()
            pincel = self.paleta2.BackgroundColour
            self.fundo1.Hide()
            self.fundo3.Hide()
            self.fundo4.Hide()

    def selecao3(self,event):
        global pincel
        if not self.paleta1.BackgroundColour == 'white':
            self.fundo3.Show()
            pincel = self.paleta3.BackgroundColour
            self.fundo1.Hide()
            self.fundo2.Hide()
            self.fundo4.Hide()

    def selecao4(self,event):
        global pincel
        if not self.paleta1.BackgroundColour == 'white':
            self.fundo4.Show()
            pincel = self.paleta4.BackgroundColour
            self.fundo1.Hide()
            self.fundo3.Hide()
            self.fundo2.Hide()

    def pintar1(self,event):
        self.quadro1.SetBackgroundColour((pincel))

    def pintar2(self,event):
        self.quadro2.SetBackgroundColour((pincel))

    def pintar3(self,event):
        self.quadro3.SetBackgroundColour((pincel))

    def pintar4(self,event):
        self.quadro4.SetBackgroundColour((pincel))

    def pintar5(self,event):
        self.quadro5.SetBackgroundColour((pincel))

    def pintar6(self,event):
        self.quadro6.SetBackgroundColour((pincel))

    def pintar7(self,event):
        self.quadro7.SetBackgroundColour((pincel))

    def pintar8(self,event):
        self.quadro8.SetBackgroundColour((pincel))

    def pintar9(self,event):
        self.quadro9.SetBackgroundColour((pincel))

    def pintar10(self,event):
        self.quadro10.SetBackgroundColour((pincel))

    def pintar11(self,event):
        self.quadro11.SetBackgroundColour((pincel))

    def pintar12(self,event):
        self.quadro12.SetBackgroundColour((pincel))

    def pintar13(self,event):
        self.quadro13.SetBackgroundColour((pincel))

    def pintar14(self,event):
        self.quadro14.SetBackgroundColour((pincel))

    def pintar15(self,event):
        self.quadro15.SetBackgroundColour((pincel))

    def pintar16(self,event):
        self.quadro16.SetBackgroundColour((pincel))

    def pintar17(self,event):
        self.quadro17.SetBackgroundColour((pincel))

    def pintar18(self,event):
        self.quadro18.SetBackgroundColour((pincel))

    def pintar19(self,event):
        self.quadro19.SetBackgroundColour((pincel))

    def pintar20(self,event):
        self.quadro20.SetBackgroundColour((pincel))

    def pintar21(self,event):
        self.quadro21.SetBackgroundColour((pincel))

    def pintar22(self,event):
        self.quadro22.SetBackgroundColour((pincel))

    def pintar23(self,event):
        self.quadro23.SetBackgroundColour((pincel))

    def pintar24(self,event):
        self.quadro24.SetBackgroundColour((pincel))

    def pintar25(self,event):
        self.quadro25.SetBackgroundColour((pincel))

    def resetar(self,event):
        global pincel
        pincel = 'white'
        self.paleta1.SetBackgroundColour((255,255,255))
        self.paleta2.SetBackgroundColour((255,255,255))
        self.paleta3.SetBackgroundColour((255,255,255))
        self.paleta4.SetBackgroundColour((255,255,255))
        self.fundo1.Hide()
        self.fundo2.Hide()
        self.fundo3.Hide()
        self.fundo4.Hide()
        self.quadro1.SetBackgroundColour((255,255,255))
        self.quadro2.SetBackgroundColour((255,255,255))
        self.quadro3.SetBackgroundColour((255,255,255))
        self.quadro4.SetBackgroundColour((255,255,255))
        self.quadro5.SetBackgroundColour((255,255,255))
        self.quadro6.SetBackgroundColour((255,255,255))
        self.quadro7.SetBackgroundColour((255,255,255))
        self.quadro8.SetBackgroundColour((255,255,255))
        self.quadro9.SetBackgroundColour((255,255,255))
        self.quadro10.SetBackgroundColour((255,255,255))
        self.quadro11.SetBackgroundColour((255,255,255))
        self.quadro12.SetBackgroundColour((255,255,255))
        self.quadro13.SetBackgroundColour((255,255,255))
        self.quadro14.SetBackgroundColour((255,255,255))
        self.quadro15.SetBackgroundColour((255,255,255))
        self.quadro16.SetBackgroundColour((255,255,255))
        self.quadro17.SetBackgroundColour((255,255,255))
        self.quadro18.SetBackgroundColour((255,255,255))
        self.quadro19.SetBackgroundColour((255,255,255))
        self.quadro20.SetBackgroundColour((255,255,255))
        self.quadro21.SetBackgroundColour((255,255,255))
        self.quadro22.SetBackgroundColour((255,255,255))
        self.quadro23.SetBackgroundColour((255,255,255))
        self.quadro24.SetBackgroundColour((255,255,255))
        self.quadro25.SetBackgroundColour((255,255,255)) 

        self.quadro1.SetSize(100,100)
        self.quadro2.SetSize(100,100) 
        self.quadro3.SetSize(100,100) 
        self.quadro4.SetSize(100,100) 
        self.quadro5.SetSize(100,100) 
        self.quadro6.SetSize(100,100) 
        self.quadro7.SetSize(100,100) 
        self.quadro8.SetSize(100,100) 
        self.quadro9.SetSize(100,100) 
        self.quadro10.SetSize(100,100) 
        self.quadro11.SetSize(100,100) 
        self.quadro12.SetSize(100,100) 
        self.quadro13.SetSize(100,100) 
        self.quadro14.SetSize(100,100) 
        self.quadro15.SetSize(100,100) 
        self.quadro16.SetSize(100,100) 
        self.quadro17.SetSize(100,100) 
        self.quadro18.SetSize(100,100) 
        self.quadro19.SetSize(100,100) 
        self.quadro20.SetSize(100,100) 
        self.quadro21.SetSize(100,100) 
        self.quadro22.SetSize(100,100) 
        self.quadro23.SetSize(100,100) 
        self.quadro24.SetSize(100,100) 
        self.quadro25.SetSize(100,100)

        self.edTamanho.SetValue('') 

    def redefinir(self,event):
        tamanho = int(self.edTamanho.GetValue())
        if tamanho in range(50,111):
            self.quadro1.SetSize(tamanho,tamanho)
            self.quadro2.SetSize(tamanho,tamanho)
            self.quadro3.SetSize(tamanho,tamanho)
            self.quadro4.SetSize(tamanho,tamanho)
            self.quadro5.SetSize(tamanho,tamanho)
            self.quadro6.SetSize(tamanho,tamanho)
            self.quadro7.SetSize(tamanho,tamanho)
            self.quadro8.SetSize(tamanho,tamanho)
            self.quadro9.SetSize(tamanho,tamanho)
            self.quadro10.SetSize(tamanho,tamanho)
            self.quadro11.SetSize(tamanho,tamanho)
            self.quadro12.SetSize(tamanho,tamanho)
            self.quadro13.SetSize(tamanho,tamanho)
            self.quadro14.SetSize(tamanho,tamanho)
            self.quadro15.SetSize(tamanho,tamanho)
            self.quadro16.SetSize(tamanho,tamanho)
            self.quadro17.SetSize(tamanho,tamanho)
            self.quadro18.SetSize(tamanho,tamanho)
            self.quadro19.SetSize(tamanho,tamanho)
            self.quadro20.SetSize(tamanho,tamanho)
            self.quadro21.SetSize(tamanho,tamanho)
            self.quadro22.SetSize(tamanho,tamanho)
            self.quadro23.SetSize(tamanho,tamanho)
            self.quadro24.SetSize(tamanho,tamanho)
            self.quadro25.SetSize(tamanho,tamanho)
        else:
            alerta = wx.MessageBox('O valor não deve ser menor que 50 ou maior que 110', 'Atenção!',wx.OK | wx.ICON_WARNING)
            return alerta

app = wx.App()
frame = PaletadeCores(parent=None, id=-1)
frame.Show()
app.MainLoop()