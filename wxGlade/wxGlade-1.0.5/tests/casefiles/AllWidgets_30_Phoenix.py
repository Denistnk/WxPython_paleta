#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
import gettext
import wx.adv
import wx.grid
import wx.propgrid
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class All_Widgets_Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: All_Widgets_Frame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((800, 417))
        self.SetTitle(_("All Widgets"))
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.ArtProvider.GetBitmap(wx.ART_TIP, wx.ART_OTHER, (32, 32)))
        self.SetIcon(_icon)

        # Menu Bar
        self.All_Widgets_menubar = wx.MenuBar()
        global mn_IDUnix; mn_IDUnix = wx.NewId()
        global mn_IDWindows; mn_IDWindows = wx.NewId()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_OPEN, _("&Open"), _("Open an existing document"))
        wxglade_tmp_menu.Append(wx.ID_CLOSE, _("&Close file"), _("Close current document"))
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_EXIT, _("E&xit"), _("Finish program"))
        self.All_Widgets_menubar.Append(wxglade_tmp_menu, _("&File"))
        wxglade_tmp_menu = wx.Menu()
        self.All_Widgets_menubar.mn_Unix = wxglade_tmp_menu.Append(mn_IDUnix, _("Unix"), _("Use Unix line endings"), wx.ITEM_RADIO)
        self.Bind(wx.EVT_MENU, self.onSelectUnix, id=mn_IDUnix)
        self.All_Widgets_menubar.mn_Windows = wxglade_tmp_menu.Append(mn_IDWindows, _("Windows"), _("Use Windows line endings"), wx.ITEM_RADIO)
        self.Bind(wx.EVT_MENU, self.onSelectWindows, id=mn_IDWindows)
        wxglade_tmp_menu.AppendSeparator()
        self.All_Widgets_menubar.mn_RemoveTabs = wxglade_tmp_menu.Append(wx.ID_ANY, _("Remove Tabs"), _("Remove all leading tabs"), wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU, self.onRemoveTabs, self.All_Widgets_menubar.mn_RemoveTabs)
        self.All_Widgets_menubar.Append(wxglade_tmp_menu, _("&Edit"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_HELP, _("Manual"), _("Show the application manual"))
        self.Bind(wx.EVT_MENU, self.onShowManual, id=wx.ID_HELP)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_ABOUT, _("About"), _("Show the About dialog"))
        self.All_Widgets_menubar.Append(wxglade_tmp_menu, _("&Help"))
        self.SetMenuBar(self.All_Widgets_menubar)
        # Menu Bar end

        self.All_Widgets_statusbar = self.CreateStatusBar(1, wx.STB_ELLIPSIZE_MIDDLE | wx.STB_SHOW_TIPS | wx.STB_SIZEGRIP)
        self.All_Widgets_statusbar.SetStatusWidths([-1])
        # statusbar fields
        All_Widgets_statusbar_fields = [_("All Widgets statusbar")]
        for i in range(len(All_Widgets_statusbar_fields)):
            self.All_Widgets_statusbar.SetStatusText(All_Widgets_statusbar_fields[i], i)

        # Tool Bar
        self.All_Widgets_toolbar = wx.ToolBar(self, -1)
        self.All_Widgets_toolbar.AddTool(wx.ID_UP, _("UpDown"), wx.ArtProvider.GetBitmap(wx.ART_GO_UP, wx.ART_OTHER, (32, 32)), wx.ArtProvider.GetBitmap(wx.ART_GO_DOWN, wx.ART_OTHER, (32, 32)), wx.ITEM_CHECK, _("Up or Down"), _("Up or Down"))
        self.All_Widgets_toolbar.AddTool(wx.ID_OPEN, _("Open"), wx.Bitmap(32, 32), wx.NullBitmap, wx.ITEM_NORMAL, _("Open a new file"), _("Open a new file"))
        self.SetToolBar(self.All_Widgets_toolbar)
        self.All_Widgets_toolbar.Realize()
        # Tool Bar end

        sizer_1 = wx.FlexGridSizer(3, 1, 0, 0)

        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=wx.NB_BOTTOM)
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)

        self.notebook_1_wxBitmapButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxBitmapButton, _("wxBitmapButton"))

        sizer_13 = wx.FlexGridSizer(2, 2, 0, 0)

        self.bitmap_button_icon1 = wx.BitmapButton(self.notebook_1_wxBitmapButton, wx.ID_ANY, wx.Bitmap("icon.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_icon1.SetSize(self.bitmap_button_icon1.GetBestSize())
        self.bitmap_button_icon1.SetDefault()
        sizer_13.Add(self.bitmap_button_icon1, 1, wx.ALL | wx.EXPAND, 5)

        self.bitmap_button_empty1 = wx.BitmapButton(self.notebook_1_wxBitmapButton, wx.ID_ANY, wx.Bitmap(10, 10))
        self.bitmap_button_empty1.SetSize(self.bitmap_button_empty1.GetBestSize())
        self.bitmap_button_empty1.SetDefault()
        sizer_13.Add(self.bitmap_button_empty1, 1, wx.ALL | wx.EXPAND, 5)

        self.bitmap_button_icon2 = wx.BitmapButton(self.notebook_1_wxBitmapButton, wx.ID_ANY, wx.Bitmap("icon.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE | wx.BU_BOTTOM)
        self.bitmap_button_icon2.SetBitmapDisabled(wx.Bitmap(32, 32))
        self.bitmap_button_icon2.SetSize(self.bitmap_button_icon2.GetBestSize())
        self.bitmap_button_icon2.SetDefault()
        sizer_13.Add(self.bitmap_button_icon2, 1, wx.ALL | wx.EXPAND, 5)

        self.bitmap_button_art = wx.BitmapButton(self.notebook_1_wxBitmapButton, wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_GO_UP, wx.ART_OTHER, (32, 32)), style=wx.BORDER_NONE | wx.BU_BOTTOM)
        self.bitmap_button_art.SetSize(self.bitmap_button_art.GetBestSize())
        self.bitmap_button_art.SetDefault()
        sizer_13.Add(self.bitmap_button_art, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxButton, _("wxButton"))

        sizer_28 = wx.BoxSizer(wx.HORIZONTAL)

        self.button_3 = wx.Button(self.notebook_1_wxButton, wx.ID_BOLD, "")
        sizer_28.Add(self.button_3, 0, wx.ALL, 5)

        self.notebook_1_wxCalendarCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxCalendarCtrl, _("wxCalendarCtrl"))

        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)

        self.calendar_ctrl_1 = wx.adv.CalendarCtrl(self.notebook_1_wxCalendarCtrl, wx.ID_ANY, style=wx.adv.CAL_MONDAY_FIRST | wx.adv.CAL_SEQUENTIAL_MONTH_SELECTION | wx.adv.CAL_SHOW_SURROUNDING_WEEKS | wx.adv.CAL_SHOW_WEEK_NUMBERS)
        sizer_12.Add(self.calendar_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxGenericCalendarCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxGenericCalendarCtrl, _("wxGenericCalendarCtrl"))

        sizer_27 = wx.BoxSizer(wx.HORIZONTAL)

        self.generic_calendar_ctrl_1 = wx.adv.GenericCalendarCtrl(self.notebook_1_wxGenericCalendarCtrl, wx.ID_ANY, style=wx.adv.CAL_MONDAY_FIRST)
        sizer_27.Add(self.generic_calendar_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxCheckBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxCheckBox, _("wxCheckBox"))

        sizer_21 = wx.GridSizer(2, 3, 0, 0)

        self.checkbox_1 = wx.CheckBox(self.notebook_1_wxCheckBox, wx.ID_ANY, _("one (unchecked)"))
        sizer_21.Add(self.checkbox_1, 0, wx.EXPAND, 0)

        self.checkbox_2 = wx.CheckBox(self.notebook_1_wxCheckBox, wx.ID_ANY, _("two (checked)"))
        self.checkbox_2.SetValue(1)
        sizer_21.Add(self.checkbox_2, 0, wx.EXPAND, 0)

        self.checkbox_3 = wx.CheckBox(self.notebook_1_wxCheckBox, wx.ID_ANY, _("three"), style=wx.CHK_2STATE)
        sizer_21.Add(self.checkbox_3, 0, wx.EXPAND, 0)

        self.checkbox_4 = wx.CheckBox(self.notebook_1_wxCheckBox, wx.ID_ANY, _("four (unchecked)"), style=wx.CHK_3STATE)
        self.checkbox_4.Set3StateValue(wx.CHK_UNCHECKED)
        sizer_21.Add(self.checkbox_4, 0, wx.EXPAND, 0)

        self.checkbox_5 = wx.CheckBox(self.notebook_1_wxCheckBox, wx.ID_ANY, _("five (checked)"), style=wx.CHK_3STATE | wx.CHK_ALLOW_3RD_STATE_FOR_USER)
        self.checkbox_5.Set3StateValue(wx.CHK_CHECKED)
        sizer_21.Add(self.checkbox_5, 0, wx.EXPAND, 0)

        self.checkbox_6 = wx.CheckBox(self.notebook_1_wxCheckBox, wx.ID_ANY, _("six (undetermined)"), style=wx.CHK_3STATE | wx.CHK_ALLOW_3RD_STATE_FOR_USER)
        self.checkbox_6.Set3StateValue(wx.CHK_UNDETERMINED)
        sizer_21.Add(self.checkbox_6, 0, wx.EXPAND, 0)

        self.notebook_1_wxCheckListBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxCheckListBox, _("wxCheckListBox"))

        sizer_26 = wx.BoxSizer(wx.HORIZONTAL)

        self.check_list_box_1 = wx.CheckListBox(self.notebook_1_wxCheckListBox, wx.ID_ANY, choices=[_("one"), _("two"), _("three"), _("four")])
        self.check_list_box_1.SetSelection(2)
        sizer_26.Add(self.check_list_box_1, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxChoice = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxChoice, _("wxChoice"))

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)

        self.choice_empty = wx.Choice(self.notebook_1_wxChoice, wx.ID_ANY, choices=[])
        sizer_5.Add(self.choice_empty, 1, wx.ALL, 5)

        self.choice_filled = wx.Choice(self.notebook_1_wxChoice, wx.ID_ANY, choices=[_("Item 1"), _("Item 2 (pre-selected)")])
        self.choice_filled.SetSelection(1)
        sizer_5.Add(self.choice_filled, 1, wx.ALL, 5)

        self.notebook_1_wxComboBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxComboBox, _("wxComboBox"))

        sizer_6 = wx.BoxSizer(wx.VERTICAL)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)

        self.combo_box_empty = wx.ComboBox(self.notebook_1_wxComboBox, wx.ID_ANY, choices=[], style=0)
        sizer_7.Add(self.combo_box_empty, 1, wx.ALL, 5)

        self.combo_box_filled = wx.ComboBox(self.notebook_1_wxComboBox, wx.ID_ANY, choices=[_("Item 1 (pre-selected)"), _("Item 2")], style=0)
        self.combo_box_filled.SetSelection(0)
        sizer_7.Add(self.combo_box_filled, 1, wx.ALL, 5)

        self.notebook_1_wxDatePickerCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxDatePickerCtrl, _("wxDatePickerCtrl"))

        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)

        self.datepicker_ctrl_1 = wx.adv.DatePickerCtrl(self.notebook_1_wxDatePickerCtrl, wx.ID_ANY, style=wx.adv.DP_SHOWCENTURY)
        sizer_17.Add(self.datepicker_ctrl_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.notebook_1_wxGauge = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxGauge, _("wxGauge"))

        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)

        self.gauge_1 = wx.Gauge(self.notebook_1_wxGauge, wx.ID_ANY, 20)
        sizer_15.Add(self.gauge_1, 1, wx.ALL, 5)

        self.notebook_1_wxGrid = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxGrid, _("wxGrid"))

        sizer_19 = wx.BoxSizer(wx.HORIZONTAL)

        self.grid_1 = wx.grid.Grid(self.notebook_1_wxGrid, wx.ID_ANY, size=(1, 1))
        self.grid_1.CreateGrid(10, 3)
        self.grid_1.SetSelectionMode(wx.grid.Grid.SelectColumns)
        self.grid_1.SetColLabelValue(1, _("B\nB"))
        sizer_19.Add(self.grid_1, 1, wx.EXPAND, 0)

        self.notebook_1_wxHyperlinkCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxHyperlinkCtrl, _("wxHyperlinkCtrl"))

        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)

        self.hyperlink_1 = wx.adv.HyperlinkCtrl(self.notebook_1_wxHyperlinkCtrl, wx.ID_ANY, _("Homepage wxGlade"), _("http://wxglade.sf.net"))
        sizer_20.Add(self.hyperlink_1, 0, wx.ALL, 5)

        self.notebook_1_wxListBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxListBox, _("wxListBox"))

        sizer_4 = wx.BoxSizer(wx.VERTICAL)

        self.list_box_empty = wx.ListBox(self.notebook_1_wxListBox, wx.ID_ANY, choices=[], style=0)
        sizer_4.Add(self.list_box_empty, 1, wx.ALL | wx.EXPAND, 5)

        self.list_box_filled = wx.ListBox(self.notebook_1_wxListBox, wx.ID_ANY, choices=[_("Item 1"), _("Item 2 (pre-selected)")], style=wx.LB_MULTIPLE | wx.LB_SORT)
        self.list_box_filled.SetSelection(1)
        sizer_4.Add(self.list_box_filled, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxListCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxListCtrl, _("wxListCtrl"))

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)

        self.list_ctrl_1 = wx.ListCtrl(self.notebook_1_wxListCtrl, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_REPORT)
        sizer_3.Add(self.list_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxPropertyGridManager = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxPropertyGridManager, _("wxPropertyGridManager"))

        sizer_34 = wx.BoxSizer(wx.HORIZONTAL)

        self.property_grid_2 = wx.propgrid.PropertyGridManager(self.notebook_1_wxPropertyGridManager, wx.ID_ANY, style=wx.propgrid.PG_ALPHABETIC_MODE)
        sizer_34.Add(self.property_grid_2, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxRadioBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxRadioBox, _("wxRadioBox"))

        grid_sizer_1 = wx.GridSizer(2, 2, 0, 0)

        self.radio_box_empty1 = wx.RadioBox(self.notebook_1_wxRadioBox, wx.ID_ANY, _("radio_box_empty1"), choices=[""], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        grid_sizer_1.Add(self.radio_box_empty1, 1, wx.ALL | wx.EXPAND, 5)

        self.radio_box_filled1 = wx.RadioBox(self.notebook_1_wxRadioBox, wx.ID_ANY, _("radio_box_filled1"), choices=[_("choice 1"), _("choice 2 (pre-selected)"), _("choice 3")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_filled1.SetSelection(1)
        grid_sizer_1.Add(self.radio_box_filled1, 1, wx.ALL | wx.EXPAND, 5)

        self.radio_box_empty2 = wx.RadioBox(self.notebook_1_wxRadioBox, wx.ID_ANY, _("radio_box_empty2"), choices=[""], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        grid_sizer_1.Add(self.radio_box_empty2, 1, wx.ALL | wx.EXPAND, 5)

        self.radio_box_filled2 = wx.RadioBox(self.notebook_1_wxRadioBox, wx.ID_ANY, _("radio_box_filled2"), choices=[_("choice 1 %"), _("choice 2 (pre-selected)")], majorDimension=0, style=wx.RA_SPECIFY_COLS)
        self.radio_box_filled2.SetSelection(1)
        grid_sizer_1.Add(self.radio_box_filled2, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxRadioButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxRadioButton, _("wxRadioButton"))

        sizer_8 = wx.StaticBoxSizer(wx.StaticBox(self.notebook_1_wxRadioButton, wx.ID_ANY, _("My RadioButton Group")), wx.HORIZONTAL)

        grid_sizer_2 = wx.FlexGridSizer(3, 2, 0, 0)
        sizer_8.Add(grid_sizer_2, 1, wx.EXPAND, 0)

        self.radio_btn_1 = wx.RadioButton(self.notebook_1_wxRadioButton, wx.ID_ANY, _("Alice"), style=wx.RB_GROUP)
        grid_sizer_2.Add(self.radio_btn_1, 1, wx.ALL | wx.EXPAND, 5)

        self.text_ctrl_1 = wx.TextCtrl(self.notebook_1_wxRadioButton, wx.ID_ANY, "")
        grid_sizer_2.Add(self.text_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)

        self.radio_btn_2 = wx.RadioButton(self.notebook_1_wxRadioButton, wx.ID_ANY, _("Bob"))
        grid_sizer_2.Add(self.radio_btn_2, 1, wx.ALL | wx.EXPAND, 5)

        self.text_ctrl_2 = wx.TextCtrl(self.notebook_1_wxRadioButton, wx.ID_ANY, "")
        grid_sizer_2.Add(self.text_ctrl_2, 1, wx.ALL | wx.EXPAND, 5)

        self.radio_btn_3 = wx.RadioButton(self.notebook_1_wxRadioButton, wx.ID_ANY, _("Malroy"))
        grid_sizer_2.Add(self.radio_btn_3, 1, wx.ALL | wx.EXPAND, 5)

        self.text_ctrl_3 = wx.TextCtrl(self.notebook_1_wxRadioButton, wx.ID_ANY, "")
        grid_sizer_2.Add(self.text_ctrl_3, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxSlider = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxSlider, _("wxSlider"))

        sizer_22 = wx.BoxSizer(wx.HORIZONTAL)

        self.slider_1 = wx.Slider(self.notebook_1_wxSlider, wx.ID_ANY, 5, 0, 10, style=0)
        sizer_22.Add(self.slider_1, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxSpinButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxSpinButton, _("wxSpinButton (with wxTextCtrl)"))

        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)

        self.tc_spin_button = wx.TextCtrl(self.notebook_1_wxSpinButton, wx.ID_ANY, _("1"), style=wx.TE_RIGHT)
        sizer_16.Add(self.tc_spin_button, 1, wx.ALL, 5)

        self.spin_button = wx.SpinButton(self.notebook_1_wxSpinButton, wx.ID_ANY )
        sizer_16.Add(self.spin_button, 1, wx.ALL, 5)

        self.notebook_1_wxSpinCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxSpinCtrl, _("wxSpinCtrl"))

        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)

        self.spin_ctrl_1 = wx.SpinCtrl(self.notebook_1_wxSpinCtrl, wx.ID_ANY, "4", min=0, max=100, style=wx.ALIGN_RIGHT | wx.SP_ARROW_KEYS)
        sizer_14.Add(self.spin_ctrl_1, 1, wx.ALL, 5)

        self.notebook_1_wxSplitterWindow_horizontal = wx.ScrolledWindow(self.notebook_1, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.notebook_1_wxSplitterWindow_horizontal.SetScrollRate(10, 10)
        self.notebook_1.AddPage(self.notebook_1_wxSplitterWindow_horizontal, _("wxSplitterWindow (horizontally)"))

        sizer_29 = wx.BoxSizer(wx.HORIZONTAL)

        self.splitter_1 = wx.SplitterWindow(self.notebook_1_wxSplitterWindow_horizontal, wx.ID_ANY, style=0)
        self.splitter_1.SetBackgroundColour(wx.Colour(255, 0, 0))
        self.splitter_1.SetMinimumPaneSize(20)
        sizer_29.Add(self.splitter_1, 1, wx.ALL | wx.EXPAND, 5)

        self.splitter_1_pane_1 = wx.Panel(self.splitter_1, wx.ID_ANY)

        sizer_30 = wx.BoxSizer(wx.HORIZONTAL)

        self.label_top_pane = wx.StaticText(self.splitter_1_pane_1, wx.ID_ANY, _("top pane"))
        sizer_30.Add(self.label_top_pane, 1, wx.ALL | wx.EXPAND, 5)

        self.splitter_1_pane_2 = wx.Panel(self.splitter_1, wx.ID_ANY)

        sizer_31 = wx.BoxSizer(wx.HORIZONTAL)

        self.label_buttom_pane = wx.StaticText(self.splitter_1_pane_2, wx.ID_ANY, _("bottom pane"))
        sizer_31.Add(self.label_buttom_pane, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxSplitterWindow_vertical = wx.ScrolledWindow(self.notebook_1, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.notebook_1_wxSplitterWindow_vertical.SetScrollRate(10, 10)
        self.notebook_1.AddPage(self.notebook_1_wxSplitterWindow_vertical, _("wxSplitterWindow (vertically)"))

        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)

        self.splitter_2 = wx.SplitterWindow(self.notebook_1_wxSplitterWindow_vertical, wx.ID_ANY, style=0)
        self.splitter_2.SetMinimumPaneSize(20)
        sizer_25.Add(self.splitter_2, 1, wx.ALL | wx.EXPAND, 5)

        self.splitter_2_pane_1 = wx.Panel(self.splitter_2, wx.ID_ANY)

        sizer_32 = wx.BoxSizer(wx.VERTICAL)

        self.label_left_pane = wx.StaticText(self.splitter_2_pane_1, wx.ID_ANY, _("left pane"))
        sizer_32.Add(self.label_left_pane, 1, wx.ALL | wx.EXPAND, 5)

        self.splitter_2_pane_2 = wx.Panel(self.splitter_2, wx.ID_ANY)

        sizer_33 = wx.BoxSizer(wx.VERTICAL)

        self.label_right_pane = wx.StaticText(self.splitter_2_pane_2, wx.ID_ANY, _("right pane"))
        sizer_33.Add(self.label_right_pane, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxStaticBitmap = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxStaticBitmap, _("wxStaticBitmap"))

        sizer_11 = wx.BoxSizer(wx.VERTICAL)

        self.bitmap_empty = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, wx.Bitmap(32, 32))
        sizer_11.Add(self.bitmap_empty, 1, wx.ALL | wx.EXPAND, 5)

        self.bitmap_file = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, wx.Bitmap("icon.png", wx.BITMAP_TYPE_ANY))
        sizer_11.Add(self.bitmap_file, 1, wx.ALL | wx.EXPAND, 5)

        self.bitmap_nofile = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, wx.Bitmap("non-existing.bmp", wx.BITMAP_TYPE_ANY))
        sizer_11.Add(self.bitmap_nofile, 1, wx.ALL | wx.EXPAND, 5)

        self.bitmap_art = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_PRINT, wx.ART_OTHER, (32, 32)))
        sizer_11.Add(self.bitmap_art, 1, wx.ALL | wx.EXPAND, 5)

        self.bitmap_null = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, wx.NullBitmap)
        sizer_11.Add(self.bitmap_null, 1, wx.ALL | wx.EXPAND, 5)

        self.bitmap_null_sized = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, wx.Bitmap(50, 50))
        self.bitmap_null_sized.SetMinSize((50, 50))
        sizer_11.Add(self.bitmap_null_sized, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxStaticLine = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxStaticLine, _("wxStaticLine"))

        sizer_9 = wx.BoxSizer(wx.VERTICAL)

        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9.Add(sizer_10, 1, wx.EXPAND, 0)

        self.static_line_2 = wx.StaticLine(self.notebook_1_wxStaticLine, wx.ID_ANY, style=wx.LI_VERTICAL)
        sizer_10.Add(self.static_line_2, 1, wx.ALL | wx.EXPAND, 5)

        self.static_line_3 = wx.StaticLine(self.notebook_1_wxStaticLine, wx.ID_ANY, style=wx.LI_VERTICAL)
        sizer_10.Add(self.static_line_3, 1, wx.ALL | wx.EXPAND, 5)

        self.static_line_4 = wx.StaticLine(self.notebook_1_wxStaticLine, wx.ID_ANY)
        sizer_9.Add(self.static_line_4, 1, wx.ALL | wx.EXPAND, 5)

        self.static_line_5 = wx.StaticLine(self.notebook_1_wxStaticLine, wx.ID_ANY)
        sizer_9.Add(self.static_line_5, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxStaticText = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxStaticText, _("wxStaticText"))

        grid_sizer_3 = wx.FlexGridSizer(1, 3, 0, 0)

        self.label_1 = wx.StaticText(self.notebook_1_wxStaticText, wx.ID_ANY, _("red text (RGB)"), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.label_1.SetForegroundColour(wx.Colour(255, 0, 0))
        grid_sizer_3.Add(self.label_1, 1, wx.ALL | wx.EXPAND, 5)

        self.label_4 = wx.StaticText(self.notebook_1_wxStaticText, wx.ID_ANY, _("black on red (RGB)"), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.label_4.SetBackgroundColour(wx.Colour(255, 0, 0))
        self.label_4.SetToolTip(_("Background colour won't show, check documentation for more details"))
        grid_sizer_3.Add(self.label_4, 1, wx.ALL | wx.EXPAND, 5)

        self.label_5 = wx.StaticText(self.notebook_1_wxStaticText, wx.ID_ANY, _("green on pink (RGB)"), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.label_5.SetBackgroundColour(wx.Colour(255, 0, 255))
        self.label_5.SetForegroundColour(wx.Colour(0, 255, 0))
        self.label_5.SetToolTip(_("Background colour won't show, check documentation for more details"))
        grid_sizer_3.Add(self.label_5, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_Spacer = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_Spacer, _("Spacer"))

        grid_sizer_4 = wx.FlexGridSizer(1, 3, 0, 0)

        self.label_3 = wx.StaticText(self.notebook_1_Spacer, wx.ID_ANY, _("Two labels with a"))
        grid_sizer_4.Add(self.label_3, 1, wx.ALL | wx.EXPAND, 5)

        grid_sizer_4.Add((60, 20), 1, wx.ALL | wx.EXPAND, 5)

        self.label_2 = wx.StaticText(self.notebook_1_Spacer, wx.ID_ANY, _("spacer between"))
        grid_sizer_4.Add(self.label_2, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxTextCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxTextCtrl, _("wxTextCtrl"))

        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)

        self.text_ctrl = wx.TextCtrl(self.notebook_1_wxTextCtrl, wx.ID_ANY, _("This\nis\na\nmultiline\nwxTextCtrl"), style=wx.TE_CHARWRAP | wx.TE_MULTILINE | wx.TE_WORDWRAP)
        sizer_18.Add(self.text_ctrl, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_wxToggleButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxToggleButton, _("wxToggleButton"))

        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)

        self.button_2 = wx.ToggleButton(self.notebook_1_wxToggleButton, wx.ID_ANY, _("Toggle Button 1"))
        sizer_23.Add(self.button_2, 1, wx.ALL, 5)

        self.button_4 = wx.ToggleButton(self.notebook_1_wxToggleButton, wx.ID_ANY, _("Toggle Button 2"), style=wx.BU_BOTTOM | wx.BU_EXACTFIT)
        sizer_23.Add(self.button_4, 1, wx.ALL, 5)

        self.notebook_1_wxTreeCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_wxTreeCtrl, _("wxTreeCtrl"))

        sizer_24 = wx.BoxSizer(wx.HORIZONTAL)

        self.tree_ctrl_1 = wx.TreeCtrl(self.notebook_1_wxTreeCtrl, wx.ID_ANY, style=0)
        sizer_24.Add(self.tree_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)

        self.static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        sizer_1.Add(self.static_line_1, 0, wx.ALL | wx.EXPAND, 5)

        sizer_2 = wx.FlexGridSizer(1, 2, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT, 0)

        self.button_5 = wx.Button(self, wx.ID_CLOSE, "")
        sizer_2.Add(self.button_5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.button_1 = wx.Button(self, wx.ID_OK, "", style=wx.BU_TOP)
        sizer_2.Add(self.button_1, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.notebook_1_wxTreeCtrl.SetSizer(sizer_24)

        self.notebook_1_wxToggleButton.SetSizer(sizer_23)

        self.notebook_1_wxTextCtrl.SetSizer(sizer_18)

        self.notebook_1_Spacer.SetSizer(grid_sizer_4)

        self.notebook_1_wxStaticText.SetSizer(grid_sizer_3)

        self.notebook_1_wxStaticLine.SetSizer(sizer_9)

        self.notebook_1_wxStaticBitmap.SetSizer(sizer_11)

        self.splitter_2_pane_2.SetSizer(sizer_33)

        self.splitter_2_pane_1.SetSizer(sizer_32)

        self.splitter_2.SplitVertically(self.splitter_2_pane_1, self.splitter_2_pane_2)

        self.notebook_1_wxSplitterWindow_vertical.SetSizer(sizer_25)

        self.splitter_1_pane_2.SetSizer(sizer_31)

        self.splitter_1_pane_1.SetSizer(sizer_30)

        self.splitter_1.SplitHorizontally(self.splitter_1_pane_1, self.splitter_1_pane_2)

        self.notebook_1_wxSplitterWindow_horizontal.SetSizer(sizer_29)

        self.notebook_1_wxSpinCtrl.SetSizer(sizer_14)

        self.notebook_1_wxSpinButton.SetSizer(sizer_16)

        self.notebook_1_wxSlider.SetSizer(sizer_22)

        self.notebook_1_wxRadioButton.SetSizer(sizer_8)

        self.notebook_1_wxRadioBox.SetSizer(grid_sizer_1)

        self.notebook_1_wxPropertyGridManager.SetSizer(sizer_34)

        self.notebook_1_wxListCtrl.SetSizer(sizer_3)

        self.notebook_1_wxListBox.SetSizer(sizer_4)

        self.notebook_1_wxHyperlinkCtrl.SetSizer(sizer_20)

        self.notebook_1_wxGrid.SetSizer(sizer_19)

        self.notebook_1_wxGauge.SetSizer(sizer_15)

        self.notebook_1_wxDatePickerCtrl.SetSizer(sizer_17)

        self.notebook_1_wxComboBox.SetSizer(sizer_6)

        self.notebook_1_wxChoice.SetSizer(sizer_5)

        self.notebook_1_wxCheckListBox.SetSizer(sizer_26)

        self.notebook_1_wxCheckBox.SetSizer(sizer_21)

        self.notebook_1_wxGenericCalendarCtrl.SetSizer(sizer_27)

        self.notebook_1_wxCalendarCtrl.SetSizer(sizer_12)

        self.notebook_1_wxButton.SetSizer(sizer_28)

        sizer_13.AddGrowableRow(0)
        sizer_13.AddGrowableRow(1)
        sizer_13.AddGrowableCol(0)
        sizer_13.AddGrowableCol(1)
        self.notebook_1_wxBitmapButton.SetSizer(sizer_13)

        sizer_1.AddGrowableRow(0)
        sizer_1.AddGrowableCol(0)
        self.SetSizer(sizer_1)
        sizer_1.SetSizeHints(self)

        self.Layout()
        self.Centre()

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNotebookPageChanged, self.notebook_1)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnNotebookPageChanging, self.notebook_1)
        self.Bind(wx.EVT_NAVIGATION_KEY, self.OnBitmapButtonPanelNavigationKey)
        self.Bind(wx.EVT_BUTTON, self.onStartConverting, self.button_1)
        # end wxGlade

    def onSelectUnix(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'onSelectUnix' not implemented!")
        event.Skip()

    def onSelectWindows(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'onSelectWindows' not implemented!")
        event.Skip()

    def onRemoveTabs(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'onRemoveTabs' not implemented!")
        event.Skip()

    def onShowManual(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'onShowManual' not implemented!")
        event.Skip()

    def OnNotebookPageChanged(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'OnNotebookPageChanged' not implemented!")
        event.Skip()

    def OnNotebookPageChanging(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'OnNotebookPageChanging' not implemented!")
        event.Skip()

    def OnBitmapButtonPanelNavigationKey(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'OnBitmapButtonPanelNavigationKey' not implemented!")
        event.Skip()

    def onStartConverting(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'onStartConverting' not implemented!")
        event.Skip()

# end of class All_Widgets_Frame

if __name__ == "__main__":
    gettext.install("AllWidgets30App") # replace with the appropriate catalog name

    AllWidgets30App = wx.PySimpleApp()
    All_Widgets = All_Widgets_Frame(None, wx.ID_ANY, "")
    AllWidgets30App.SetTopWindow(All_Widgets)
    All_Widgets.Show()
    AllWidgets30App.MainLoop()
