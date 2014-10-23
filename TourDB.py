#Boa:Frame:Frame1
import wx
import sqlite3
import AddDialog 

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1ADD, wxID_FRAME1DELETE, wxID_FRAME1EDIT, 
 wxID_FRAME1FIND, wxID_FRAME1PANEL1, wxID_FRAME1STATUSBAR1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(325, 188), size=wx.Size(911, 445),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(911, 445))

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self.statusBar1.SetToolTipString(u'statusBar1')
        self.statusBar1.SetThemeEnabled(False)
        self.statusBar1.SetStatusText(u'')
        self.statusBar1.SetFieldsCount(0)
        self.statusBar1.SetHelpText(u'')
        self.statusBar1.SetLabel(u'')
        self.SetStatusBar(self.statusBar1)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(624, 304), size=wx.Size(240, 104),
              style=wx.TAB_TRAVERSAL)

        self.Add = wx.Button(id=wxID_FRAME1ADD, label=u'Add', name=u'Add',
              parent=self, pos=wx.Point(48, 376), size=wx.Size(96, 32),
              style=0)
        self.Add.Bind(wx.EVT_BUTTON, self.OnAddButton, id=wxID_FRAME1ADD)

        self.Edit = wx.Button(id=wxID_FRAME1EDIT, label=u'Edit', name=u'Edit',
              parent=self, pos=wx.Point(200, 376), size=wx.Size(104, 32),
              style=0)
        self.Edit.Bind(wx.EVT_BUTTON, self.OnEditButton, id=wxID_FRAME1EDIT)

        self.Find = wx.Button(id=wxID_FRAME1FIND, label=u'Find', name=u'Find',
              parent=self, pos=wx.Point(352, 376), size=wx.Size(104, 32),
              style=0)
        self.Find.Bind(wx.EVT_BUTTON, self.OnFindButton, id=wxID_FRAME1FIND)

        self.Delete = wx.Button(id=wxID_FRAME1DELETE, label=u'Delete',
              name=u'Delete', parent=self, pos=wx.Point(496, 376),
              size=wx.Size(104, 32), style=0)
        self.Delete.Bind(wx.EVT_BUTTON, self.OnDeleteButton,
              id=wxID_FRAME1DELETE)

    def __init__(self, parent):
        self._init_ctrls(parent)

    #def OnButton1Button(self, event):
     #   event.Skip()

    #def OnButton2Button(self, event):
     #   event.Skip()

    def OnAddButton(self, event):
        
        dlg = AddDialog.Dialog1(self)
        #try:
        
        if dlg.ShowModal() == wx.ID_OK:
            Fname = dlg.txtName.GetValue()
            Sname = dlg.txtSecond_name.GetValue()
            Tname = dlg.txtThird_Name.GetValue()
            DBirth = (dlg.dateDate_of_birth.GetValue())
            CiBirth = dlg.txtCity_of_birth.GetValue()
            CoBirth = dlg.txtCountry_of_birth.GetValue()
            CPassport = dlg.txtCitizen_passport.GetValue()
            FPasport = dlg.txtForeign_Passport.GetValue()
            FPassportStart = (dlg.dateDate_of_passport_start.GetValue())
            FPassportFin = (dlg.dateDate_of_Passport_fin.GetValue())
            INN = int(dlg.txtINN.GetValue())
            Countries = dlg.txtCountries.GetValue()
            HAdress = dlg.txtHome_adress.GetValue()
            Phone = int(dlg.txtPhone.GetValue())
            Notes = dlg.txtNotes.GetValue()
            
            connection = sqlite3.connect('Touristdb.db')
            cursor = connection.cursor()
            sql = "SELECT * FROM Tourist WHERE FirstName = '" + Fname + "'"
            cursor.execute(sql)
            recordset = cursor.fetchall()
            if len(recordset) <> 0:
                dlg2 = wx.MessageDialog(self, "Tourist already exists", "TouristDB", wx.OK)
                dlg2.ShowModal() # Show it
                dlg2.Destroy() # finally destroy it when finished.
            else:
                cursor.execute("INSERT INTO Tourist VALUES (null, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (Fname, Sname, Tname, DBirth, CiBirth, CoBirth, CPassport, FPassport, FPassportStart, FPassportFin, INN, Countries, HAdress, Phone, Notes))

                connection.commit()
# A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
                dlg2 = wx.MessageDialog( self, "Tourist Added", "CDDB", wx.OK)
                dlg2.ShowModal() # Show it
                dlg2.Destroy() # finally destroy it when finished.
        #finally:
                cursor.Close()
                connection.Close()
                dlg.Destroy()

    def OnEditButton(self, event):
        event.Skip()

    def OnFindButton(self, event):
        event.Skip()

    def OnDeleteButton(self, event):
        event.Skip()
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()

