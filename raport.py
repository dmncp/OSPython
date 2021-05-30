# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raport.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from collections import OrderedDict

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QDate, QTime
import PDFgen as PDFgenerator
from datetime import datetime


class Ui_RaportWindow(object):
    def __init__(self):
        self.rs = None
        self.ps = None
        self.driver_list = None
        self.aleader_list = None
        self.sleader_list = None
        self.def_time = QTime(00, 00, 0)

    def setupUi(self, RaportWindow):
        RaportWindow.setObjectName("RaportWindow")
        RaportWindow.resize(935, 933)
        RaportWindow.setFixedSize(935, 933)
        self.centralwidget = QtWidgets.QWidget(RaportWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(580, 10, 20, 851))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 490, 561, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 131, 16))
        self.label_3.setObjectName("label_3")
        self.place_name = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.place_name.setGeometry(QtCore.QRect(20, 100, 541, 21))
        self.place_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.place_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.place_name.setObjectName("place_name")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 131, 16))
        self.label_4.setObjectName("label_4")
        self.accident_type = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.accident_type.setGeometry(QtCore.QRect(20, 150, 541, 41))
        self.accident_type.setObjectName("accident_type")
        self.injured = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.injured.setGeometry(QtCore.QRect(20, 220, 541, 21))
        self.injured.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.injured.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.injured.setObjectName("injured")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 131, 16))
        self.label_6.setObjectName("label_6")
        self.perpetrator = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.perpetrator.setGeometry(QtCore.QRect(20, 270, 541, 21))
        self.perpetrator.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.perpetrator.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.perpetrator.setObjectName("perpetrator")
        self.accident_type_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.accident_type_2.setGeometry(QtCore.QRect(20, 320, 541, 61))
        self.accident_type_2.setObjectName("accident_type_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 300, 131, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 0, 551, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.return_hour = QtWidgets.QTimeEdit(self.centralwidget)
        self.return_hour.setGeometry(QtCore.QRect(140, 410, 111, 22))
        self.return_hour.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.return_hour.setObjectName("return_hour")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(140, 390, 131, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 390, 121, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(260, 390, 131, 16))
        self.label_11.setObjectName("label_11")
        self.depot_hour = QtWidgets.QTimeEdit(self.centralwidget)
        self.depot_hour.setGeometry(QtCore.QRect(260, 410, 111, 22))
        self.depot_hour.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.depot_hour.setObjectName("depot_hour")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 440, 131, 16))
        self.label_12.setObjectName("label_12")
        self.counter_state = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.counter_state.setGeometry(QtCore.QRect(20, 460, 101, 21))
        self.counter_state.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.counter_state.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.counter_state.setObjectName("counter_state")
        self.KM_to_place = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.KM_to_place.setGeometry(QtCore.QRect(140, 460, 121, 21))
        self.KM_to_place.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.KM_to_place.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.KM_to_place.setObjectName("KM_to_place")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(140, 440, 131, 16))
        self.label_13.setObjectName("label_13")
        self.section_current = QtWidgets.QListWidget(self.centralwidget)
        self.section_current.setGeometry(QtCore.QRect(20, 520, 241, 192))
        self.section_current.setUniformItemSizes(True)
        self.section_current.setObjectName("section_current")
        self.all_members = QtWidgets.QListWidget(self.centralwidget)
        self.all_members.setGeometry(QtCore.QRect(320, 520, 241, 192))
        self.all_members.setUniformItemSizes(True)
        self.all_members.setObjectName("all_members")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 500, 241, 20))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(320, 500, 241, 20))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.section_leader_id = QtWidgets.QComboBox(self.centralwidget)
        self.section_leader_id.setGeometry(QtCore.QRect(20, 740, 281, 22))
        self.section_leader_id.setObjectName("section_leader_id")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 720, 131, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(20, 770, 131, 16))
        self.label_17.setObjectName("label_17")
        self.action_leader_id = QtWidgets.QComboBox(self.centralwidget)
        self.action_leader_id.setGeometry(QtCore.QRect(20, 790, 281, 22))
        self.action_leader_id.setObjectName("action_leader_id")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(20, 820, 131, 16))
        self.label_18.setObjectName("label_18")
        self.driver_id = QtWidgets.QComboBox(self.centralwidget)
        self.driver_id.setGeometry(QtCore.QRect(20, 840, 281, 22))
        self.driver_id.setObjectName("driver_id")
        self.add_report_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_report_button.setGeometry(QtCore.QRect(360, 760, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.add_report_button.setFont(font)
        self.add_report_button.setObjectName("add_report_button")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(600, 0, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.at_place_date_search = QtWidgets.QDateEdit(self.centralwidget)
        self.at_place_date_search.setGeometry(QtCore.QRect(600, 120, 91, 22))
        self.at_place_date_search.setCalendarPopup(True)
        self.at_place_date_search.setObjectName("at_place_date_search")
        self.out_date_search = QtWidgets.QDateEdit(self.centralwidget)
        self.out_date_search.setGeometry(QtCore.QRect(600, 70, 91, 22))
        self.out_date_search.setCalendarPopup(True)
        self.out_date_search.setObjectName("out_date_search")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(600, 100, 131, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(600, 50, 121, 16))
        self.label_21.setObjectName("label_21")
        self.report_list_search = QtWidgets.QListWidget(self.centralwidget)
        self.report_list_search.setGeometry(QtCore.QRect(640, 210, 256, 192))
        self.report_list_search.setObjectName("report_list_search")
        self.generate_report_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_report_button.setGeometry(QtCore.QRect(610, 820, 321, 31))
        self.generate_report_button.setObjectName("generate_report_button")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(600, 150, 131, 16))
        self.label_22.setObjectName("label_22")
        self.place_name_search = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.place_name_search.setGeometry(QtCore.QRect(600, 170, 231, 21))
        self.place_name_search.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.place_name_search.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.place_name_search.setObjectName("place_name_search")
        self.action_details = QtWidgets.QTextEdit(self.centralwidget)
        self.action_details.setGeometry(QtCore.QRect(610, 430, 321, 381))
        self.action_details.setObjectName("action_details")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(610, 410, 131, 16))
        self.label_23.setObjectName("label_23")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.out_date = QtWidgets.QDateEdit(self.centralwidget)
        self.out_date.setGeometry(QtCore.QRect(20, 50, 110, 22))
        self.out_date.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.out_date.setCalendarPopup(True)
        self.out_date.setObjectName("out_date")
        self.at_place_date = QtWidgets.QDateEdit(self.centralwidget)
        self.at_place_date.setGeometry(QtCore.QRect(280, 50, 110, 22))
        self.at_place_date.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.at_place_date.setCalendarPopup(True)
        self.at_place_date.setObjectName("at_place_date")
        self.out_hour = QtWidgets.QTimeEdit(self.centralwidget)
        self.out_hour.setGeometry(QtCore.QRect(140, 50, 81, 22))
        self.out_hour.setObjectName("out_hour")
        self.at_place_hour = QtWidgets.QTimeEdit(self.centralwidget)
        self.at_place_hour.setGeometry(QtCore.QRect(400, 50, 81, 22))
        self.at_place_hour.setObjectName("at_place_hour")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(140, 30, 121, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(400, 30, 121, 16))
        self.label_25.setObjectName("label_25")
        self.edit_report_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_report_button.setGeometry(QtCore.QRect(610, 850, 321, 31))
        self.edit_report_button.setObjectName("edit_report_button")
        self.return_date = QtWidgets.QDateEdit(self.centralwidget)
        self.return_date.setGeometry(QtCore.QRect(20, 410, 110, 22))
        self.return_date.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.return_date.setCalendarPopup(True)
        self.return_date.setObjectName("return_date")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(720, 50, 121, 16))
        self.label_26.setObjectName("label_26")
        self.out_hour_date = QtWidgets.QTimeEdit(self.centralwidget)
        self.out_hour_date.setGeometry(QtCore.QRect(720, 70, 81, 22))
        self.out_hour_date.setObjectName("out_hour_date")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(720, 100, 121, 16))
        self.label_27.setObjectName("label_27")
        self.at_place_search = QtWidgets.QTimeEdit(self.centralwidget)
        self.at_place_search.setGeometry(QtCore.QRect(720, 120, 81, 22))
        self.at_place_search.setObjectName("at_place_search")
        RaportWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RaportWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 21))
        self.menubar.setObjectName("menubar")
        RaportWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RaportWindow)
        self.statusbar.setObjectName("statusbar")
        RaportWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RaportWindow)
        QtCore.QMetaObject.connectSlotsByName(RaportWindow)

    def retranslateUi(self, RaportWindow):
        _translate = QtCore.QCoreApplication.translate
        RaportWindow.setWindowTitle(_translate("RaportWindow", "Raporty"))
        self.label.setText(_translate("RaportWindow", "Data wyjazdu"))
        self.label_2.setText(_translate("RaportWindow", "Data na miejscu"))
        self.label_3.setText(_translate("RaportWindow", "Miejsce zdarzenia"))
        self.label_4.setText(_translate("RaportWindow", "Rodzaj zdarzenia"))
        self.label_5.setText(_translate("RaportWindow", "Poszkodowany"))
        self.label_6.setText(_translate("RaportWindow", "Sprawca"))
        self.label_7.setText(_translate("RaportWindow", "Szczegóły zdarzenia"))
        self.label_8.setText(_translate("RaportWindow", "Nowy raport"))
        self.label_9.setText(_translate("RaportWindow", "Godzina zakończenia"))
        self.label_10.setText(_translate("RaportWindow", "Data powrotu"))
        self.label_11.setText(_translate("RaportWindow", "Godzina w remizie"))
        self.label_12.setText(_translate("RaportWindow", "Stan licznika"))
        self.label_13.setText(_translate("RaportWindow", "KM do miejsca zdarzenia"))
        self.label_14.setText(_translate("RaportWindow", "Sekcja na akcji"))
        self.label_15.setText(_translate("RaportWindow", "Wszyscy członkowie sekcji"))
        self.label_16.setText(_translate("RaportWindow", "Dowódca sekcji"))
        self.label_17.setText(_translate("RaportWindow", "Dowódca akcji"))
        self.label_18.setText(_translate("RaportWindow", "Kierowca"))
        self.add_report_button.setText(_translate("RaportWindow", "Dodaj raport"))
        self.label_19.setText(_translate("RaportWindow", "Archiwum raportów"))
        self.label_20.setText(_translate("RaportWindow", "Data na miejscu"))
        self.label_21.setText(_translate("RaportWindow", "Data wyjazdu"))
        self.generate_report_button.setText(_translate("RaportWindow", "Wygeneruj plik raportu"))
        self.label_22.setText(_translate("RaportWindow", "Miejsce zdarzenia"))
        self.label_23.setText(_translate("RaportWindow", "Szczegóły wybranej akcji"))
        self.pushButton_2.setText(_translate("RaportWindow", "Powrót do menu"))
        self.label_24.setText(_translate("RaportWindow", "Godzina wyjazdu"))
        self.label_25.setText(_translate("RaportWindow", "Godzina na miejscu"))
        self.edit_report_button.setText(_translate("RaportWindow", "Edytuj wybrany raport"))
        self.label_26.setText(_translate("RaportWindow", "Godzina wyjazdu"))
        self.label_27.setText(_translate("RaportWindow", "Godzina na miejscu"))

        # block of code which should remain after UI change

        self.out_date.setDate(QDate.currentDate())
        self.at_place_date.setDate(QDate.currentDate())
        self.at_place_date_search.setDate(QDate.currentDate())
        self.return_date.setDate(QDate.currentDate())
        self.edit_report_button.setDisabled(True)
        self.generate_report_button.setDisabled(True)
        self.add_report_button.clicked.connect(lambda: self.add_report())
        self.report_list_search.itemSelectionChanged.connect(lambda: self.selection_changed())
        self.all_members.itemClicked.connect(lambda: self.pick_person_all())
        self.section_current.itemClicked.connect(lambda: self.pick_person_current())
        self.all_members.itemClicked.connect(lambda: self.get_selected_members_ids())
        self.generate_report_button.clicked.connect(lambda: self.generate_chosen_pdf())
        self.place_name_search.textChanged.connect(lambda: self.filter_by_place())
        self.out_date_search.dateChanged.connect(lambda: self.filter_by_out_date())
        self.out_hour_date.dateTimeChanged.connect(lambda: self.filter_by_out_hour())
        self.at_place_search.dateTimeChanged.connect(lambda: self.filter_by_at_place_hour())
        self.at_place_date_search.dateChanged.connect(lambda: self.filter_by_at_place_date())

    def generate_chosen_pdf(self):
        chosen_report = self.report_list_search.currentItem().text()
        chosen_report_id = self.rs.get_report_id_by_fields(chosen_report)
        if chosen_report_id is not None:
            PDFgenerator.PDFgen(chosen_report_id, self.ps, self.rs)

    # report data view helpers
    def id_to_text(self, ps, id):
        person = ps.get_person_by_id(id)
        person_data = person.get("FirstName") + " " + person.get("LastName")
        return person_data

    def section_to_string(self, ps, section_table):
        section_string = ""
        print(section_table)
        for id in section_table:
            section_string += self.id_to_text(ps, id) + "\n"
        if section_string == "":
            print("Empty section")
        return section_string

    # WORKS, JUST CHECK IF REPORT HAS CORRECT KEYS!!!!!!!
    def selection_changed(self):
        # DEBUG PRINTOUTS REMOVE LATER
        self.edit_report_button.setEnabled(True)
        self.generate_report_button.setEnabled(True)
        chosen_report = self.report_list_search.currentItem().text()
        # print("Selected report data --  " + chosen_report)

        chosen_report_id = self.rs.get_report_id_by_fields(chosen_report)
        # print("Selected report id -- " + chosen_report_id)

        chosen_report_data = self.rs.get_report_data(chosen_report_id)

        printed_data = ""
        printed_data += "Data wyjazdu: " + chosen_report_data.get("out_date") + "\n"
        printed_data += "Godzina wyjazdu: " + chosen_report_data.get("out_hour") + "\n"
        printed_data += "Godzina na miejscu: " + chosen_report_data.get("at_place_hour") + "\n"
        printed_data += "Rodzaj zdarzenia: " + chosen_report_data.get("accident_type") + "\n"
        printed_data += "Miejsce zdarzenia: " + chosen_report_data.get("place_name") + "\n\n"
        print(printed_data)
        printed_data += "Skład sekcji: " + "\n" + self.section_to_string(self.ps, chosen_report_data.get(
            "section_current")) + "\n"
        printed_data += "Dowódca sekcji: " + self.id_to_text(self.ps,
                                                             chosen_report_data.get("section_leader_id")) + "\n"
        printed_data += "Dowódca akcji: " + self.id_to_text(self.ps, chosen_report_data.get("action_leader_id")) + "\n"
        printed_data += "Kierowca: " + self.id_to_text(self.ps, chosen_report_data.get("driver_id")) + "\n"
        printed_data += "Sprawca: " + chosen_report_data.get("perpetrator") + "\n"
        printed_data += "Poszkodowany: " + chosen_report_data.get("injured") + "\n"
        printed_data += "Szczegóły zdarzenia: " + chosen_report_data.get("details") + "\n"
        printed_data += "Data powrotu: " + chosen_report_data.get("return_date") + "\n"
        printed_data += "Godzina zakończenia: " + chosen_report_data.get("return_hour") + "\n"
        printed_data += "Godzina w remizie: " + chosen_report_data.get("depot_hour") + "\n"
        printed_data += "Stan licznika: " + chosen_report_data.get("counter_state") + "\n"
        printed_data += "KM do miejsca zdarzenia: " + str(chosen_report_data.get("KM_to_place")) + "\n"

        # print(printed_data)

        self.action_details.setText(printed_data)

    def pick_person_all(self):
        person_picked = self.all_members.currentItem().text()
        print(person_picked)

        self.all_members.model().removeRow(self.all_members.currentRow())
        self.section_current.addItem(person_picked)

    def pick_person_current(self):
        person_picked = self.section_current.currentItem().text()
        print(person_picked)

        self.section_current.model().removeRow(self.section_current.currentRow())
        self.all_members.addItem(person_picked)

    def add_all_people(self):
        all_people = self.ps.get_all_people()
        for key, i in all_people.items():
            if i is not None:
                self.all_members.addItem(i.get("FirstName") + "," + i.get("LastName") + "," + str(i.get("PhoneNumber")))

    # to get rid of repeating instructions

    # adds all elements to the UI item, can expand with refresh of the list later
    def set_all(self, list_all, ui_element):
        for person in list_all:
            self.ui_element.addItem(
                person.get("FirstName") + "," + person.get("LastName") + "," + str(person.get("PhoneNumber")))

    # gets id of chosen person from data in UI element, should return None if not found (should not happen in usage)
    def translate_to_id(self, text):
        person_details = text.split(",")
        p_len = len(person_details)
        p_num = person_details[p_len - 1]
        p_last = person_details[p_len - 2]
        p_first = ""
        for i in range(0, p_len - 2):
            p_first += person_details[i]
        return self.ps.check_person_existence(p_first, p_last, int(p_num))

    # end of these

    # next three can be replaced with set_all
    def set_all_drivers(self):
        for driver in self.driver_list:
            self.driver_id.addItem(
                driver.get("FirstName") + "," + driver.get("LastName") + "," + str(driver.get("PhoneNumber")))

    def set_all_aleaders(self):
        for aleader in self.aleader_list:
            self.action_leader_id.addItem(
                aleader.get("FirstName") + "," + aleader.get("LastName") + "," + str(aleader.get("PhoneNumber")))

    def set_all_sleaders(self):
        for sleader in self.sleader_list:
            self.section_leader_id.addItem(
                sleader.get("FirstName") + "," + sleader.get("LastName") + "," + str(sleader.get("PhoneNumber")))

    # get reports in report list
    # maybe more universal one?
    # "" as place makes place check skipped

    # delete everything, set default values
    def clean_window(self):
        self.set_current_values()
        # T O D O - clean everything else

    # to call just before window switch
    def refresh(self):
        self.clean_window()
        # should load drivers etc again here

    # sets date values to current ones
    def set_current_values(self):
        self.out_date.setDate(QDate.currentDate())
        self.at_place_date.setDate(QDate.currentDate())
        self.at_place_date_search.setDate(QDate.currentDate())
        self.return_date.setDate(QDate.currentDate())


    def sort_reports_by_date(self, reports_list):
        sorted_by_time = OrderedDict(sorted(reports_list.items(),
                                            key=lambda t: datetime.strptime(t[1]["at_place_hour"], "%H:%M")))
        sorted_list = sorted(sorted_by_time.items(),
                             key=lambda date: datetime.strptime(date[1]["at_place_date"], "%d-%m-%Y"))
        return OrderedDict(sorted_list)

    def filter_by_place(self):
        all_reports = self.filter_prepare()
        for key, i in all_reports.items():
            if i is not None and ((self.place_name_search.toPlainText().lower() in i.get("place_name").lower())
                                  or self.place_name_search.toPlainText() == ""):
                self.report_list_search.addItem(
                    i.get("at_place_date") + "," + i.get("at_place_hour") + "," + i.get("place_name"))

    def filter_by_out_date(self):
        all_reports = self.filter_prepare()
        for key, i in all_reports.items():
            if i is not None and (self.out_date_search.date().toString('dd-MM-yyyy') == i.get("out_date")):
                self.report_list_search.addItem(
                    i.get("at_place_date") + "," + i.get("at_place_hour") + "," + i.get("place_name"))

    def filter_by_out_hour(self):
        all_reports = self.filter_prepare()
        for key, i in all_reports.items():
            if i is not None and (self.out_hour_date.dateTime().toString('HH:mm') == i.get("out_hour")):
                self.report_list_search.addItem(
                    i.get("at_place_date") + "," + i.get("at_place_hour") + "," + i.get("place_name"))

    def filter_by_at_place_hour(self):
        all_reports = self.filter_prepare()
        for key, i in all_reports.items():
            if i is not None and (self.at_place_search.dateTime().toString('HH:mm') == i.get("at_place_hour")):
                self.report_list_search.addItem(
                    i.get("at_place_date") + "," + i.get("at_place_hour") + "," + i.get("place_name"))

    def filter_by_at_place_date(self):
        all_reports = self.filter_prepare()
        for key, i in all_reports.items():
            if i is not None and (self.at_place_date_search.date().toString('dd-MM-yyyy') == i.get("at_place_date")):
                self.report_list_search.addItem(
                    i.get("at_place_date") + "," + i.get("at_place_hour") + "," + i.get("place_name"))

    def filter_prepare(self):
        all_reports = self.rs.get_all_reports()
        all_reports = self.sort_reports_by_date(all_reports)
        self.report_list_search.clear()
        return all_reports

    def get_all_reports(self):
        all_reports = self.rs.get_all_reports()
        all_reports = self.sort_reports_by_date(all_reports)
        for key, i in all_reports.items():
            if i is not None:
                self.report_list_search.addItem(
                    i.get("at_place_date") + "," + i.get("at_place_hour") + "," + i.get("place_name"))

    def get_selected_members_ids(self):
        all_text_data = [str(self.section_current.item(i).text()) for i in range(self.section_current.count())]
        print(all_text_data)
        for i in range(len(all_text_data)):
            all_text_data[i] = self.translate_to_id(all_text_data[i])
        return all_text_data

    def check_special_field_in_current(self, group):
        included = 0
        for i in range(0, self.section_current.count()):
            if self.section_current.item(i).text() == group.currentText():
                included = 1
                break
        if included == 0:
            return False
        else:
            return True

    # check if report is valid (18 checks? some can be skipped)
    def validate(self):
        # we need to check if:
        #         - miejsce zdarzenia - is there | DONE
        #         - rodzaj zdarzenia - is there | DONE
        #         - stan licznika - is there, is digits | DONE
        #         - km do miejsca zdarzenia - is there, is digits | DONE
        #         - sekcja na akcji - is there, contains below (maybe not section leader?) | THERE IS CHECK IF NOT EMPTY
        #         - dowódca sekcji(?), akcji, kierowca powinni być na liście "sekcja na akcji" | DONE
        #remove test printouts later

        print("Before every validation")
        if self.section_current.count() == 0:
            return False
        print("Before acc")
        if self.accident_type.toPlainText() == "":
            return False
        if self.place_name.toPlainText() == "":
            return False
        print("Before counter")
        if self.counter_state.toPlainText() != "":
            if not self.counter_state.toPlainText().isdecimal():
                return False
        if self.counter_state.toPlainText() == "":
            return False

        print("Before KM")
        if self.KM_to_place.toPlainText() != "":
            if not self.KM_to_place.toPlainText().isdecimal():
                return False
        if self.KM_to_place.toPlainText() == "":
            return False

        print("Before existence in current section")

        #this could be in a function?
        if not self.check_special_field_in_current(self.section_leader_id):
            return False

        if not self.check_special_field_in_current(self.action_leader_id):
            return False

        if not self.check_special_field_in_current(self.driver_id):
            return False

        print("Validated")
        return True


    def refresh_reports_list(self):
        self.report_list_search.clear()
        self.get_all_reports()

    # add report with current data
    def add_report(self):

        if self.validate() is not True:
            print("Invalid report")
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Raport został źle wypełniony!')
            error_dialog.exec_()

        else:
            # get id of driver, section leader, action leader

            driver_details = self.driver_id.currentText()
            sleader_details = self.section_leader_id.currentText()
            aleader_details = self.action_leader_id.currentText()

            d_id = self.translate_to_id(driver_details)
            sl_id = self.translate_to_id(sleader_details)
            al_id = self.translate_to_id(aleader_details)

            self.rs.add_report(self.KM_to_place.toPlainText(),
                               self.accident_type.toPlainText(),
                               self.at_place_date.dateTime().toString('dd-MM-yyyy'),
                               self.at_place_hour.dateTime().toString('HH:mm'),
                               self.counter_state.toPlainText(),
                               self.depot_hour.dateTime().toString('HH:mm'),
                               self.injured.toPlainText(),
                               self.out_date.date().toString('dd-MM-yyyy'),
                               self.out_hour.dateTime().toString('HH:mm'),
                               self.perpetrator.toPlainText(),
                               self.place_name.toPlainText(),
                               self.return_date.date().toString('dd-MM-yyyy'),
                               self.return_hour.dateTime().toString('HH:mm'),
                               self.get_selected_members_ids(),
                               sl_id,
                               0,
                               al_id,
                               d_id,
                               self.accident_type_2.toPlainText())

            self.refresh_reports_list()

    def giveValue(self):
        if self.report_list_search.currentItem() is not None:
            chosen_report = self.report_list_search.currentItem().text()
            return self.rs.get_report_id_by_fields(chosen_report)
        else:
            return None

    def getValue(self, report_id):
        pass
