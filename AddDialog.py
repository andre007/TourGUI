#Boa:Dialog:Dialog1

import wx
import TourDB

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BTNCANCEL, wxID_DIALOG1BTNOK, 
 wxID_DIALOG1DATEDATE_OF_BIRTH, wxID_DIALOG1DATEDATE_OF_PASSPORT_FIN, 
 wxID_DIALOG1DATEDATE_OF_PASSPORT_START, wxID_DIALOG1FNAME, wxID_DIALOG1NOTES, 
 wxID_DIALOG1STATICTEXT10, wxID_DIALOG1STATICTEXT11, wxID_DIALOG1STATICTEXT12, 
 wxID_DIALOG1STATICTEXT13, wxID_DIALOG1STATICTEXT14, wxID_DIALOG1STATICTEXT15, 
 wxID_DIALOG1STATICTEXT2, wxID_DIALOG1STATICTEXT3, wxID_DIALOG1STATICTEXT4, 
 wxID_DIALOG1STATICTEXT5, wxID_DIALOG1STATICTEXT6, wxID_DIALOG1STATICTEXT7, 
 wxID_DIALOG1STATICTEXT8, wxID_DIALOG1STATICTEXT9, 
 wxID_DIALOG1TXTCITIZEN_PASSPORT, wxID_DIALOG1TXTCITY_OF_BIRTH, 
 wxID_DIALOG1TXTCOUNTRIES, wxID_DIALOG1TXTCOUNTRY_OF_BIRTH, 
 wxID_DIALOG1TXTFOREIGN_PASSPORT, wxID_DIALOG1TXTHOME_ADRESS, 
 wxID_DIALOG1TXTINN, wxID_DIALOG1TXTNAME, wxID_DIALOG1TXTPHONE, 
 wxID_DIALOG1TXTSECOND_NAME, wxID_DIALOG1TXTTHIRD_NAME, 
] = [wx.NewId() for _init_ctrls in range(33)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(420, 80), size=wx.Size(944, 445),
              style=wx.DEFAULT_DIALOG_STYLE, title='Dialog1')
        self.SetClientSize(wx.Size(944, 445))

        self.Fname = wx.StaticText(id=wxID_DIALOG1FNAME, label=u'First Name',
              name=u'Fname', parent=self, pos=wx.Point(24, 16),
              size=wx.Size(104, 17), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label=u'Second Name', name='staticText2', parent=self,
              pos=wx.Point(24, 40), size=wx.Size(120, 17), style=0)

        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3,
              label=u'Third Name(optional)', name='staticText3', parent=self,
              pos=wx.Point(24, 64), size=wx.Size(146, 17), style=0)

        self.staticText4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4,
              label=u'Date of birth', name='staticText4', parent=self,
              pos=wx.Point(24, 88), size=wx.Size(136, 17), style=0)

        self.staticText5 = wx.StaticText(id=wxID_DIALOG1STATICTEXT5,
              label=u'City of birth', name='staticText5', parent=self,
              pos=wx.Point(24, 112), size=wx.Size(136, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_DIALOG1STATICTEXT6,
              label=u'Country of birth', name='staticText6', parent=self,
              pos=wx.Point(24, 136), size=wx.Size(136, 17), style=0)

        self.staticText7 = wx.StaticText(id=wxID_DIALOG1STATICTEXT7,
              label=u'Citizen passport', name='staticText7', parent=self,
              pos=wx.Point(24, 160), size=wx.Size(136, 17), style=0)

        self.staticText8 = wx.StaticText(id=wxID_DIALOG1STATICTEXT8,
              label=u'Foreign passport', name='staticText8', parent=self,
              pos=wx.Point(24, 184), size=wx.Size(136, 17), style=0)

        self.staticText9 = wx.StaticText(id=wxID_DIALOG1STATICTEXT9,
              label=u'Foreign passport starts:', name='staticText9',
              parent=self, pos=wx.Point(24, 208), size=wx.Size(163, 17),
              style=0)

        self.staticText10 = wx.StaticText(id=wxID_DIALOG1STATICTEXT10,
              label=u'Foreign passport fins:', name='staticText10', parent=self,
              pos=wx.Point(24, 232), size=wx.Size(147, 17), style=0)

        self.staticText11 = wx.StaticText(id=wxID_DIALOG1STATICTEXT11,
              label=u'INN', name='staticText11', parent=self, pos=wx.Point(24,
              256), size=wx.Size(136, 17), style=0)

        self.staticText12 = wx.StaticText(id=wxID_DIALOG1STATICTEXT12,
              label=u'Countries', name='staticText12', parent=self,
              pos=wx.Point(24, 280), size=wx.Size(136, 17), style=0)

        self.staticText13 = wx.StaticText(id=wxID_DIALOG1STATICTEXT13,
              label=u'Home adress', name='staticText13', parent=self,
              pos=wx.Point(24, 304), size=wx.Size(136, 17), style=0)

        self.staticText14 = wx.StaticText(id=wxID_DIALOG1STATICTEXT14,
              label=u'phone', name='staticText14', parent=self, pos=wx.Point(24,
              328), size=wx.Size(136, 17), style=0)

        self.staticText15 = wx.StaticText(id=wxID_DIALOG1STATICTEXT15,
              label=u'Notes', name='staticText15', parent=self, pos=wx.Point(24,
              352), size=wx.Size(136, 17), style=0)

        self.txtName = wx.TextCtrl(id=wxID_DIALOG1TXTNAME, name=u'txtName',
              parent=self, pos=wx.Point(200, 16), size=wx.Size(536, 24),
              style=0, value=u'')

        self.txtSecond_name = wx.TextCtrl(id=wxID_DIALOG1TXTSECOND_NAME,
              name=u'txtSecond_name', parent=self, pos=wx.Point(200, 40),
              size=wx.Size(536, 24), style=0, value=u'')

        self.txtThird_Name = wx.TextCtrl(id=wxID_DIALOG1TXTTHIRD_NAME,
              name=u'txtThird_Name', parent=self, pos=wx.Point(200, 64),
              size=wx.Size(536, 24), style=0, value=u'')

        self.txtCity_of_birth = wx.TextCtrl(id=wxID_DIALOG1TXTCITY_OF_BIRTH,
              name=u'txtCity_of_birth', parent=self, pos=wx.Point(200, 112),
              size=wx.Size(536, 24), style=0, value=u'')

        self.txtCountry_of_birth = wx.TextCtrl(id=wxID_DIALOG1TXTCOUNTRY_OF_BIRTH,
              name=u'txtCountry_of_birth', parent=self, pos=wx.Point(200, 136),
              size=wx.Size(536, 24), style=0, value=u'')

        self.txtCitizen_passport = wx.TextCtrl(id=wxID_DIALOG1TXTCITIZEN_PASSPORT,
              name=u'txtCitizen_passport', parent=self, pos=wx.Point(200, 160),
              size=wx.Size(536, 27), style=0, value=u'')

        self.txtForeign_Passport = wx.TextCtrl(id=wxID_DIALOG1TXTFOREIGN_PASSPORT,
              name=u'txtForeign_Passport', parent=self, pos=wx.Point(200, 184),
              size=wx.Size(536, 27), style=0, value=u'')

        self.txtINN = wx.TextCtrl(id=wxID_DIALOG1TXTINN, name=u'txtINN',
              parent=self, pos=wx.Point(200, 256), size=wx.Size(536, 24),
              style=0, value=u'')

        self.txtCountries = wx.TextCtrl(id=wxID_DIALOG1TXTCOUNTRIES,
              name=u'txtCountries', parent=self, pos=wx.Point(200, 280),
              size=wx.Size(536, 24), style=0, value=u'')

        self.txtHome_adress = wx.TextCtrl(id=wxID_DIALOG1TXTHOME_ADRESS,
              name=u'txtHome_adress', parent=self, pos=wx.Point(200, 304),
              size=wx.Size(536, 24), style=0, value=u'')

        self.txtPhone = wx.TextCtrl(id=wxID_DIALOG1TXTPHONE, name=u'txtPhone',
              parent=self, pos=wx.Point(200, 328), size=wx.Size(536, 27),
              style=0, value=u'')

        self.dateDate_of_birth = wx.DatePickerCtrl(id=wxID_DIALOG1DATEDATE_OF_BIRTH,
              name=u'dateDate_of_birth', parent=self, pos=wx.Point(200, 88),
              size=wx.Size(133, 24), style=wx.DP_SHOWCENTURY)

        self.dateDate_of_passport_start = wx.DatePickerCtrl(id=wxID_DIALOG1DATEPICKEDATEDATE_OF_PASSPORT_STARTRCTRL2,
              name=u'datePickedateDate_of_passport_startrCtrl2', parent=self,
              pos=wx.Point(200, 208), size=wx.Size(136, 24),
              style=wx.DP_SHOWCENTURY)

        self.dateDate_of_Passport_fin = wx.DatePickerCtrl(id=wxID_DIALOG1DATEDATE_OF_PASSPORT_FIN,
              name=u'dateDate_of_Passport_fin', parent=self, pos=wx.Point(200,
              232), size=wx.Size(136, 24), style=wx.DP_SHOWCENTURY)

        self.txtNotes = wx.TextCtrl(id=wxID_DIALOG1NOTES, name=u'Notes',
              parent=self, pos=wx.Point(200, 352), size=wx.Size(536, 88),
              style=0, value=u'')

        self.btnOK = wx.Button(id=wx.ID_OK, label=u'&OK', name=u'btnOK',
              parent=self, pos=wx.Point(824, 24), size=wx.Size(85, 32),
              style=0)
        self.btnOK.Bind(wx.EVT_BUTTON, self.OnBtnOKButton, id=wxID_DIALOG1BTNOK)

        self.btnCancel = wx.Button(id=wx.ID_CANCEL, label=u'&Cancel',
              name=u'btnCancel', parent=self, pos=wx.Point(824, 80),
              size=wx.Size(88, 29), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        event.Skip()

    def OnBtnOKButton(self, event):
        #Add()
        event.Skip()
