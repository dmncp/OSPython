from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime


class Ui_RaportEditWindow(object):
    def __init__(self):
        self.rs = None
        self.ps = None
        self.driver_list = None
        self.aleader_list = None
        self.sleader_list = None
        self.def_time = QTime(00, 00, 0)
        self.report_id = None

    def setupUi(self, RaportEditWindow):
        RaportEditWindow.setObjectName("RaportEditWindow")
        RaportEditWindow.resize(591, 920)
        RaportEditWindow.setFixedSize(591, 920)
        self.centralwidget = QtWidgets.QWidget(RaportEditWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(20, 780, 131, 16))
        self.label_17.setObjectName("label_17")
        self.all_members = QtWidgets.QListWidget(self.centralwidget)
        self.all_members.setGeometry(QtCore.QRect(320, 530, 241, 192))
        self.all_members.setUniformItemSizes(True)
        self.all_members.setObjectName("all_members")
        self.accident_type_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.accident_type_2.setGeometry(QtCore.QRect(20, 330, 541, 61))
        self.accident_type_2.setObjectName("accident_type_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 121, 16))
        self.label.setObjectName("label")
        self.KM_to_place = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.KM_to_place.setGeometry(QtCore.QRect(140, 470, 121, 21))
        self.KM_to_place.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.KM_to_place.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.KM_to_place.setObjectName("KM_to_place")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 40, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 730, 131, 16))
        self.label_16.setObjectName("label_16")
        self.accident_type = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.accident_type.setGeometry(QtCore.QRect(20, 160, 541, 41))
        self.accident_type.setObjectName("accident_type")
        self.return_date = QtWidgets.QDateEdit(self.centralwidget)
        self.return_date.setGeometry(QtCore.QRect(20, 420, 110, 22))
        self.return_date.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.return_date.setCalendarPopup(True)
        self.return_date.setObjectName("return_date")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 131, 16))
        self.label_6.setObjectName("label_6")
        self.place_name = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.place_name.setGeometry(QtCore.QRect(20, 110, 541, 21))
        self.place_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.place_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.place_name.setObjectName("place_name")
        self.injured = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.injured.setGeometry(QtCore.QRect(20, 230, 541, 21))
        self.injured.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.injured.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.injured.setObjectName("injured")
        self.driver_id = QtWidgets.QComboBox(self.centralwidget)
        self.driver_id.setGeometry(QtCore.QRect(20, 850, 281, 22))
        self.driver_id.setObjectName("driver_id")
        self.at_place_date = QtWidgets.QDateEdit(self.centralwidget)
        self.at_place_date.setGeometry(QtCore.QRect(280, 60, 110, 22))
        self.at_place_date.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.at_place_date.setCalendarPopup(True)
        self.at_place_date.setObjectName("at_place_date")
        self.return_hour = QtWidgets.QTimeEdit(self.centralwidget)
        self.return_hour.setGeometry(QtCore.QRect(140, 420, 111, 22))
        self.return_hour.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.return_hour.setObjectName("return_hour")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(140, 40, 121, 16))
        self.label_24.setObjectName("label_24")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(140, 400, 131, 16))
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 131, 16))
        self.label_5.setObjectName("label_5")
        self.perpetrator = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.perpetrator.setGeometry(QtCore.QRect(20, 280, 541, 21))
        self.perpetrator.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.perpetrator.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.perpetrator.setObjectName("perpetrator")
        self.section_current = QtWidgets.QListWidget(self.centralwidget)
        self.section_current.setGeometry(QtCore.QRect(20, 530, 241, 192))
        self.section_current.setUniformItemSizes(True)
        self.section_current.setObjectName("section_current")
        self.at_place_hour = QtWidgets.QTimeEdit(self.centralwidget)
        self.at_place_hour.setGeometry(QtCore.QRect(400, 60, 81, 22))
        self.at_place_hour.setObjectName("at_place_hour")
        self.out_date = QtWidgets.QDateEdit(self.centralwidget)
        self.out_date.setGeometry(QtCore.QRect(20, 60, 110, 22))
        self.out_date.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.out_date.setCalendarPopup(True)
        self.out_date.setObjectName("out_date")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 500, 561, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.out_hour = QtWidgets.QTimeEdit(self.centralwidget)
        self.out_hour.setGeometry(QtCore.QRect(140, 60, 81, 22))
        self.out_hour.setObjectName("out_hour")
        self.counter_state = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.counter_state.setGeometry(QtCore.QRect(20, 470, 101, 21))
        self.counter_state.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.counter_state.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.counter_state.setObjectName("counter_state")
        self.section_leader_id = QtWidgets.QComboBox(self.centralwidget)
        self.section_leader_id.setGeometry(QtCore.QRect(20, 750, 281, 22))
        self.section_leader_id.setObjectName("section_leader_id")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 310, 131, 16))
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 131, 16))
        self.label_4.setObjectName("label_4")
        self.update_report_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_report_button.setGeometry(QtCore.QRect(340, 790, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.update_report_button.setFont(font)
        self.update_report_button.setObjectName("update_report_button")
        self.action_leader_id = QtWidgets.QComboBox(self.centralwidget)
        self.action_leader_id.setGeometry(QtCore.QRect(20, 800, 281, 22))
        self.action_leader_id.setObjectName("action_leader_id")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(260, 400, 131, 16))
        self.label_11.setObjectName("label_11")
        self.depot_hour = QtWidgets.QTimeEdit(self.centralwidget)
        self.depot_hour.setGeometry(QtCore.QRect(260, 420, 111, 22))
        self.depot_hour.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.depot_hour.setObjectName("depot_hour")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(140, 450, 131, 16))
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 450, 131, 16))
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(320, 510, 241, 20))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(20, 830, 131, 16))
        self.label_18.setObjectName("label_18")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 510, 241, 20))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(400, 40, 121, 16))
        self.label_25.setObjectName("label_25")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 400, 121, 16))
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 551, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.close_report = QtWidgets.QCheckBox(self.centralwidget)
        self.close_report.setGeometry(QtCore.QRect(350, 760, 141, 17))
        self.close_report.setObjectName("close_report")
        RaportEditWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RaportEditWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 21))
        self.menubar.setObjectName("menubar")
        RaportEditWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RaportEditWindow)
        self.statusbar.setObjectName("statusbar")
        RaportEditWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RaportEditWindow)
        QtCore.QMetaObject.connectSlotsByName(RaportEditWindow)

    def retranslateUi(self, RaportEditWindow):
        _translate = QtCore.QCoreApplication.translate
        RaportEditWindow.setWindowTitle(_translate("RaportEditWindow", "Edycja raportu"))
        self.label_17.setText(_translate("RaportEditWindow", "Dow??dca akcji"))
        self.label.setText(_translate("RaportEditWindow", "Data wyjazdu"))
        self.label_2.setText(_translate("RaportEditWindow", "Data na miejscu"))
        self.label_16.setText(_translate("RaportEditWindow", "Dow??dca sekcji"))
        self.label_6.setText(_translate("RaportEditWindow", "Sprawca"))
        self.label_24.setText(_translate("RaportEditWindow", "Godzina wyjazdu"))
        self.label_9.setText(_translate("RaportEditWindow", "Godzina zako??czenia"))
        self.label_5.setText(_translate("RaportEditWindow", "Poszkodowany"))
        self.label_7.setText(_translate("RaportEditWindow", "Szczeg????y zdarzenia"))
        self.label_4.setText(_translate("RaportEditWindow", "Rodzaj zdarzenia"))
        self.update_report_button.setText(_translate("RaportEditWindow", "Aktualizuj raport"))
        self.label_11.setText(_translate("RaportEditWindow", "Godzina w remizie"))
        self.label_13.setText(_translate("RaportEditWindow", "KM do miejsca zdarzenia"))
        self.label_12.setText(_translate("RaportEditWindow", "Stan licznika"))
        self.label_15.setText(_translate("RaportEditWindow", "Wszyscy cz??onkowie sekcji"))
        self.label_18.setText(_translate("RaportEditWindow", "Kierowca"))
        self.label_14.setText(_translate("RaportEditWindow", "Sekcja na akcji"))
        self.label_25.setText(_translate("RaportEditWindow", "Godzina na miejscu"))
        self.label_3.setText(_translate("RaportEditWindow", "Miejsce zdarzenia"))
        self.label_10.setText(_translate("RaportEditWindow", "Data powrotu"))
        self.label_8.setText(_translate("RaportEditWindow", "Edycja raportu"))
        self.pushButton_2.setText(_translate("RaportEditWindow", "Anuluj edycj??"))
        self.close_report.setText(_translate("RaportEditWindow", "Zamknij raport"))

        # block of code to stay starts here
        self.out_date.setDate(QDate.currentDate())
        self.at_place_date.setDate(QDate.currentDate())
        self.return_date.setDate(QDate.currentDate())
        self.all_members.itemClicked.connect(lambda: self.pick_person_all())
        self.section_current.itemClicked.connect(lambda: self.pick_person_current())
        self.all_members.itemClicked.connect(lambda: self.get_selected_members_ids())
        self.update_report_button.clicked.connect(lambda: self.update_report())

    def prepare(self, ps, rs):
        self.ps = ps
        self.rs = rs
        self.driver_list = self.ps.get_drivers()
        self.set_all_drivers()
        self.sleader_list = self.ps.get_section_leaders()
        self.set_all_sleaders()
        self.aleader_list = self.ps.get_action_leaders()
        self.set_all_aleaders()
        self.add_all_people()

    def clean_window(self):
        self.driver_list = None
        self.aleader_list = None
        self.sleader_list = None

        self.place_name.clear()
        self.accident_type.clear()
        self.injured.clear()
        self.perpetrator.clear()
        self.accident_type_2.clear()
        self.counter_state.clear()
        self.KM_to_place.clear()
        self.section_current.clear()
        self.all_members.clear()
        self.section_leader_id.clear()
        self.action_leader_id.clear()
        self.driver_id.clear()

    def prepare_window(self):

        if self.report_id is None:
            print("Bad id given")
            self.update_report_button.setDisabled(True)
        else:
            if self.rs.is_report_closed(self.report_id) != 0:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Raport jest ju?? nieedytowalny!')
                error_dialog.exec_()
                self.update_report_button.setDisabled(True)
            else:
                report_data = self.rs.get_report_data(self.report_id)
                if report_data is None:
                    print("Bad data given")
                    self.update_report_button.setDisabled(True)
                else:
                    # set fields to correct chosen report values
                    self.out_date.setDate(QDate.fromString(report_data.get("out_date"), "dd-MM-yyyy"))
                    self.out_hour.setTime(QTime.fromString(report_data.get("out_hour"), "HH:mm"))
                    self.at_place_date.setDate(QDate.fromString(report_data.get("at_place_date"), "dd-MM-yyyy"))
                    self.at_place_hour.setTime(QTime.fromString(report_data.get("at_place_hour"), "HH:mm"))
                    self.place_name.setPlainText(report_data.get("place_name"))
                    self.accident_type.setPlainText(report_data.get("accident_type"))
                    self.injured.setPlainText(report_data.get("injured"))
                    self.perpetrator.setPlainText(report_data.get("perpetrator"))
                    self.accident_type_2.setPlainText(report_data.get("details"))
                    self.return_date.setDate(QDate.fromString(report_data.get("return_date"), "dd-MM-yyyy"))
                    self.return_hour.setTime(QTime.fromString(report_data.get("return_hour"), "HH:mm"))
                    self.depot_hour.setTime(QTime.fromString(report_data.get("depot_hour"), "HH:mm"))
                    self.counter_state.setPlainText(report_data.get("counter_state"))
                    self.KM_to_place.setPlainText(report_data.get("KM_to_place"))

                    section = report_data.get("section_current")

                    for i in range(len(section)):
                        text = self.ps.id_to_box(section[i])
                        section[i] = text

                    for member in section:
                        self.all_members.model().removeRow(
                            self.all_members.row(self.all_members.findItems(member, QtCore.Qt.MatchExactly)[0]))
                        self.section_current.addItem(member)

                    driver_text = self.ps.id_to_text(report_data.get("driver_id"))
                    section_leader_text = self.ps.id_to_text(report_data.get("section_leader_id"))
                    action_leader_text = self.ps.id_to_text(report_data.get("action_leader_id"))

                    self.driver_id.setCurrentText(driver_text)
                    self.action_leader_id.setCurrentText(action_leader_text)
                    self.section_leader_id.setCurrentText(section_leader_text)

                    self.close_report.setChecked(False)

    # to call just before window switch
    def refresh(self):
        self.clean_window()
        self.driver_list = self.ps.get_drivers()
        self.set_all_drivers()
        self.sleader_list = self.ps.get_section_leaders()
        self.set_all_sleaders()
        self.aleader_list = self.ps.get_action_leaders()
        self.set_all_aleaders()
        self.add_all_people()

        self.prepare_window()

    def add_all_people(self):
        all_people = self.ps.get_all_people()
        for key, i in all_people.items():
            if i is not None and i.get("IsActive"):
                self.all_members.addItem(i.get("FirstName") + "," + i.get("LastName") + "," + str(i.get("PhoneNumber")))

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

    def pick_person_all(self):
        person_picked = self.all_members.currentItem().text()

        self.all_members.model().removeRow(self.all_members.currentRow())
        self.section_current.addItem(person_picked)

    def pick_person_current(self):
        person_picked = self.section_current.currentItem().text()

        self.section_current.model().removeRow(self.section_current.currentRow())
        self.all_members.addItem(person_picked)

    def get_selected_members_ids(self):
        all_text_data = [str(self.section_current.item(i).text()) for i in range(self.section_current.count())]
        for i in range(len(all_text_data)):
            all_text_data[i] = self.ps.translate_to_id(all_text_data[i])
        return all_text_data

    # should be nearly the same as in raport.py

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
        if not self.section_current.count():
            return False
        if not self.accident_type.toPlainText():
            return False
        if not self.place_name.toPlainText() or "," in self.place_name.toPlainText():
            return False
        if self.counter_state.toPlainText():
            if not self.counter_state.toPlainText().isdecimal():
                return False
        if not self.counter_state.toPlainText():
            return False
        if self.KM_to_place.toPlainText():
            if not self.KM_to_place.toPlainText().isdecimal():
                return False
        if not self.KM_to_place.toPlainText():
            return False

        if not self.check_special_field_in_current(self.section_leader_id):
            return False
        if not self.check_special_field_in_current(self.action_leader_id):
            return False
        if not self.check_special_field_in_current(self.driver_id):
            return False

        print("Validated")
        return True

    # upload updated report
    def update_report(self):
        if self.validate() is not True:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Raport zosta?? ??le wype??niony!')
            error_dialog.exec_()

        else:
            self.rs.change_report_data(self.report_id,
                                       self.KM_to_place.toPlainText(),
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
                                       self.ps.translate_to_id(self.section_leader_id.currentText()),
                                       int(self.close_report.isChecked()),
                                       self.ps.translate_to_id(self.action_leader_id.currentText()),
                                       self.ps.translate_to_id(self.driver_id.currentText()),
                                       self.accident_type_2.toPlainText())

    def give_value(self):
        pass

    def get_value(self, report_id):
        self.report_id = report_id
        pass
