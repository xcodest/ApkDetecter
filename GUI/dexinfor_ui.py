# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dexinfor_ui.ui'
#
# Created: Sat Jan 17 17:38:21 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DexInfo(object):
    def setupUi(self, DexInfo):
        DexInfo.setObjectName(_fromUtf8("DexInfo"))
        DexInfo.setWindowModality(QtCore.Qt.WindowModal)
        DexInfo.setEnabled(True)
        DexInfo.resize(581, 422)
        DexInfo.setMinimumSize(QtCore.QSize(581, 422))
        DexInfo.setMaximumSize(QtCore.QSize(581, 422))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Andy/Desktop/201.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DexInfo.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(DexInfo)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 561, 401))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lab_magic = QtGui.QLabel(self.groupBox)
        self.lab_magic.setGeometry(QtCore.QRect(6, 20, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lab_magic.setFont(font)
        self.lab_magic.setObjectName(_fromUtf8("lab_magic"))
        self.lab_checksum = QtGui.QLabel(self.groupBox)
        self.lab_checksum.setGeometry(QtCore.QRect(6, 50, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lab_checksum.setFont(font)
        self.lab_checksum.setObjectName(_fromUtf8("lab_checksum"))
        self.lab_dex_file_size = QtGui.QLabel(self.groupBox)
        self.lab_dex_file_size.setGeometry(QtCore.QRect(6, 82, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lab_dex_file_size.setFont(font)
        self.lab_dex_file_size.setObjectName(_fromUtf8("lab_dex_file_size"))
        self.lab_header_size = QtGui.QLabel(self.groupBox)
        self.lab_header_size.setGeometry(QtCore.QRect(6, 112, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lab_header_size.setFont(font)
        self.lab_header_size.setObjectName(_fromUtf8("lab_header_size"))
        self.lab_endian_tag = QtGui.QLabel(self.groupBox)
        self.lab_endian_tag.setGeometry(QtCore.QRect(6, 144, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lab_endian_tag.setFont(font)
        self.lab_endian_tag.setObjectName(_fromUtf8("lab_endian_tag"))
        self.label_link_size = QtGui.QLabel(self.groupBox)
        self.label_link_size.setGeometry(QtCore.QRect(6, 176, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_link_size.setFont(font)
        self.label_link_size.setObjectName(_fromUtf8("label_link_size"))
        self.label_link_off = QtGui.QLabel(self.groupBox)
        self.label_link_off.setGeometry(QtCore.QRect(6, 208, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_link_off.setFont(font)
        self.label_link_off.setObjectName(_fromUtf8("label_link_off"))
        self.label_map_off = QtGui.QLabel(self.groupBox)
        self.label_map_off.setGeometry(QtCore.QRect(6, 238, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_map_off.setFont(font)
        self.label_map_off.setObjectName(_fromUtf8("label_map_off"))
        self.label_string_ids_size = QtGui.QLabel(self.groupBox)
        self.label_string_ids_size.setGeometry(QtCore.QRect(6, 269, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_string_ids_size.setFont(font)
        self.label_string_ids_size.setObjectName(_fromUtf8("label_string_ids_size"))
        self.label_string_ids_off = QtGui.QLabel(self.groupBox)
        self.label_string_ids_off.setGeometry(QtCore.QRect(6, 301, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_string_ids_off.setFont(font)
        self.label_string_ids_off.setObjectName(_fromUtf8("label_string_ids_off"))
        self.label_field_ids_size = QtGui.QLabel(self.groupBox)
        self.label_field_ids_size.setGeometry(QtCore.QRect(287, 114, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_field_ids_size.setFont(font)
        self.label_field_ids_size.setObjectName(_fromUtf8("label_field_ids_size"))
        self.label_proto_ids_size = QtGui.QLabel(self.groupBox)
        self.label_proto_ids_size.setGeometry(QtCore.QRect(287, 51, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_proto_ids_size.setFont(font)
        self.label_proto_ids_size.setObjectName(_fromUtf8("label_proto_ids_size"))
        self.label_method_ids_size = QtGui.QLabel(self.groupBox)
        self.label_method_ids_size.setGeometry(QtCore.QRect(287, 177, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_method_ids_size.setFont(font)
        self.label_method_ids_size.setObjectName(_fromUtf8("label_method_ids_size"))
        self.label_field_ids_off = QtGui.QLabel(self.groupBox)
        self.label_field_ids_off.setGeometry(QtCore.QRect(287, 145, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_field_ids_off.setFont(font)
        self.label_field_ids_off.setObjectName(_fromUtf8("label_field_ids_off"))
        self.label_method_ids_off = QtGui.QLabel(self.groupBox)
        self.label_method_ids_off.setGeometry(QtCore.QRect(287, 207, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_method_ids_off.setFont(font)
        self.label_method_ids_off.setObjectName(_fromUtf8("label_method_ids_off"))
        self.label_data_size = QtGui.QLabel(self.groupBox)
        self.label_data_size.setGeometry(QtCore.QRect(287, 302, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_data_size.setFont(font)
        self.label_data_size.setObjectName(_fromUtf8("label_data_size"))
        self.label_proto_ids_off = QtGui.QLabel(self.groupBox)
        self.label_proto_ids_off.setGeometry(QtCore.QRect(287, 83, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_proto_ids_off.setFont(font)
        self.label_proto_ids_off.setObjectName(_fromUtf8("label_proto_ids_off"))
        self.label_type_ids_off = QtGui.QLabel(self.groupBox)
        self.label_type_ids_off.setGeometry(QtCore.QRect(287, 20, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_type_ids_off.setFont(font)
        self.label_type_ids_off.setObjectName(_fromUtf8("label_type_ids_off"))
        self.label_class_defs_size = QtGui.QLabel(self.groupBox)
        self.label_class_defs_size.setGeometry(QtCore.QRect(287, 238, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_class_defs_size.setFont(font)
        self.label_class_defs_size.setObjectName(_fromUtf8("label_class_defs_size"))
        self.label_class_defs_off = QtGui.QLabel(self.groupBox)
        self.label_class_defs_off.setGeometry(QtCore.QRect(287, 271, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_class_defs_off.setFont(font)
        self.label_class_defs_off.setObjectName(_fromUtf8("label_class_defs_off"))
        self.label_type_ids_size = QtGui.QLabel(self.groupBox)
        self.label_type_ids_size.setGeometry(QtCore.QRect(6, 333, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_type_ids_size.setFont(font)
        self.label_type_ids_size.setObjectName(_fromUtf8("label_type_ids_size"))
        self.label_data_off = QtGui.QLabel(self.groupBox)
        self.label_data_off.setGeometry(QtCore.QRect(287, 334, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_data_off.setFont(font)
        self.label_data_off.setObjectName(_fromUtf8("label_data_off"))
        self.text_magic = QtGui.QTextEdit(self.groupBox)
        self.text_magic.setEnabled(False)
        self.text_magic.setGeometry(QtCore.QRect(138, 14, 141, 27))
        self.text_magic.setFrameShape(QtGui.QFrame.Panel)
        self.text_magic.setObjectName(_fromUtf8("text_magic"))
        self.text_checksum = QtGui.QTextEdit(self.groupBox)
        self.text_checksum.setEnabled(False)
        self.text_checksum.setGeometry(QtCore.QRect(138, 45, 141, 27))
        self.text_checksum.setFrameShape(QtGui.QFrame.Panel)
        self.text_checksum.setObjectName(_fromUtf8("text_checksum"))
        self.text_file_size = QtGui.QTextEdit(self.groupBox)
        self.text_file_size.setEnabled(False)
        self.text_file_size.setGeometry(QtCore.QRect(138, 76, 141, 27))
        self.text_file_size.setFrameShape(QtGui.QFrame.Panel)
        self.text_file_size.setObjectName(_fromUtf8("text_file_size"))
        self.text_header_size = QtGui.QTextEdit(self.groupBox)
        self.text_header_size.setEnabled(False)
        self.text_header_size.setGeometry(QtCore.QRect(138, 107, 141, 27))
        self.text_header_size.setFrameShape(QtGui.QFrame.Panel)
        self.text_header_size.setObjectName(_fromUtf8("text_header_size"))
        self.text_endian_tag = QtGui.QTextEdit(self.groupBox)
        self.text_endian_tag.setEnabled(False)
        self.text_endian_tag.setGeometry(QtCore.QRect(138, 138, 141, 27))
        self.text_endian_tag.setFrameShape(QtGui.QFrame.Panel)
        self.text_endian_tag.setObjectName(_fromUtf8("text_endian_tag"))
        self.text_link_size = QtGui.QTextEdit(self.groupBox)
        self.text_link_size.setEnabled(False)
        self.text_link_size.setGeometry(QtCore.QRect(138, 170, 141, 27))
        self.text_link_size.setFrameShape(QtGui.QFrame.Panel)
        self.text_link_size.setObjectName(_fromUtf8("text_link_size"))
        self.text_link_off = QtGui.QTextEdit(self.groupBox)
        self.text_link_off.setEnabled(False)
        self.text_link_off.setGeometry(QtCore.QRect(138, 201, 141, 27))
        self.text_link_off.setFrameShape(QtGui.QFrame.Panel)
        self.text_link_off.setObjectName(_fromUtf8("text_link_off"))
        self.text_map_off = QtGui.QTextEdit(self.groupBox)
        self.text_map_off.setEnabled(False)
        self.text_map_off.setGeometry(QtCore.QRect(138, 232, 141, 27))
        self.text_map_off.setFrameShape(QtGui.QFrame.Panel)
        self.text_map_off.setObjectName(_fromUtf8("text_map_off"))
        self.text_string_ids_size = QtGui.QTextEdit(self.groupBox)
        self.text_string_ids_size.setEnabled(False)
        self.text_string_ids_size.setGeometry(QtCore.QRect(138, 264, 141, 27))
        self.text_string_ids_size.setFrameShape(QtGui.QFrame.Panel)
        self.text_string_ids_size.setObjectName(_fromUtf8("text_string_ids_size"))
        self.text_string_ids_off = QtGui.QTextEdit(self.groupBox)
        self.text_string_ids_off.setEnabled(False)
        self.text_string_ids_off.setGeometry(QtCore.QRect(138, 296, 141, 27))
        self.text_string_ids_off.setFrameShape(QtGui.QFrame.Panel)
        self.text_string_ids_off.setObjectName(_fromUtf8("text_string_ids_off"))
        self.text_type_ids_size = QtGui.QTextEdit(self.groupBox)
        self.text_type_ids_size.setEnabled(False)
        self.text_type_ids_size.setGeometry(QtCore.QRect(138, 327, 141, 27))
        self.text_type_ids_size.setFrameShape(QtGui.QFrame.Panel)
        self.text_type_ids_size.setObjectName(_fromUtf8("text_type_ids_size"))
        self.text_class_defs_off = QtGui.QTextEdit(self.groupBox)
        self.text_class_defs_off.setEnabled(False)
        self.text_class_defs_off.setGeometry(QtCore.QRect(408, 265, 141, 27))
        self.text_class_defs_off.setFrameShape(QtGui.QFrame.Panel)
        self.text_class_defs_off.setObjectName(_fromUtf8("text_class_defs_off"))
        self.text_proto_ids_off = QtGui.QTextEdit(self.groupBox)
        self.text_proto_ids_off.setEnabled(False)
        self.text_proto_ids_off.setGeometry(QtCore.QRect(408, 77, 141, 27))
        self.text_proto_ids_off.setFrameShape(QtGui.QFrame.Panel)
        self.text_proto_ids_off.setObjectName(_fromUtf8("text_proto_ids_off"))
        self.text_method_ids_off = QtGui.QTextEdit(self.groupBox)
        self.text_method_ids_off.setEnabled(False)
        self.text_method_ids_off.setGeometry(QtCore.QRect(408, 202, 141, 27))
        self.text_method_ids_off.setFrameShape(QtGui.QFrame.Panel)
        self.text_method_ids_off.setObjectName(_fromUtf8("text_method_ids_off"))
        self.text_field_ids_off = QtGui.QTextEdit(self.groupBox)
        self.text_field_ids_off.setEnabled(False)
        self.text_field_ids_off.setGeometry(QtCore.QRect(408, 139, 141, 27))
        self.text_field_ids_off.setFrameShape(QtGui.QFrame.Panel)
        self.text_field_ids_off.setObjectName(_fromUtf8("text_field_ids_off"))
        self.text_proto_ids_size = QtGui.QTextEdit(self.groupBox)
        self.text_proto_ids_size.setEnabled(False)
        self.text_proto_ids_size.setGeometry(QtCore.QRect(408, 46, 141, 27))
        self.text_proto_ids_size.setFrameShape(QtGui.QFrame.Panel)
        self.text_proto_ids_size.setObjectName(_fromUtf8("text_proto_ids_size"))
        self.text_field_ids_size = QtGui.QTextEdit(self.groupBox)
        self.text_field_ids_size.setEnabled(False)
        self.text_field_ids_size.setGeometry(QtCore.QRect(408, 108, 141, 27))
        self.text_field_ids_size.setFrameShape(QtGui.QFrame.Panel)
        self.text_field_ids_size.setObjectName(_fromUtf8("text_field_ids_size"))
        self.text_type_ids_off = QtGui.QTextEdit(self.groupBox)
        self.text_type_ids_off.setEnabled(False)
        self.text_type_ids_off.setGeometry(QtCore.QRect(408, 15, 141, 27))
        self.text_type_ids_off.setFrameShape(QtGui.QFrame.Panel)
        self.text_type_ids_off.setObjectName(_fromUtf8("text_type_ids_off"))
        self.text_data_size = QtGui.QTextEdit(self.groupBox)
        self.text_data_size.setEnabled(False)
        self.text_data_size.setGeometry(QtCore.QRect(408, 297, 141, 27))
        self.text_data_size.setFrameShape(QtGui.QFrame.Panel)
        self.text_data_size.setObjectName(_fromUtf8("text_data_size"))
        self.text_class_defs_size = QtGui.QTextEdit(self.groupBox)
        self.text_class_defs_size.setEnabled(False)
        self.text_class_defs_size.setGeometry(QtCore.QRect(408, 233, 141, 27))
        self.text_class_defs_size.setFrameShape(QtGui.QFrame.Panel)
        self.text_class_defs_size.setObjectName(_fromUtf8("text_class_defs_size"))
        self.text_method_ids_size = QtGui.QTextEdit(self.groupBox)
        self.text_method_ids_size.setEnabled(False)
        self.text_method_ids_size.setGeometry(QtCore.QRect(408, 171, 141, 27))
        self.text_method_ids_size.setFrameShape(QtGui.QFrame.Panel)
        self.text_method_ids_size.setObjectName(_fromUtf8("text_method_ids_size"))
        self.text_data_off = QtGui.QTextEdit(self.groupBox)
        self.text_data_off.setEnabled(False)
        self.text_data_off.setGeometry(QtCore.QRect(408, 328, 141, 27))
        self.text_data_off.setFrameShape(QtGui.QFrame.Panel)
        self.text_data_off.setObjectName(_fromUtf8("text_data_off"))
        self.label_sha = QtGui.QLabel(self.groupBox)
        self.label_sha.setGeometry(QtCore.QRect(10, 366, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_sha.setFont(font)
        self.label_sha.setObjectName(_fromUtf8("label_sha"))
        self.text_sha = QtGui.QTextEdit(self.groupBox)
        self.text_sha.setEnabled(False)
        self.text_sha.setGeometry(QtCore.QRect(80, 360, 471, 27))
        self.text_sha.setFrameShape(QtGui.QFrame.Panel)
        self.text_sha.setObjectName(_fromUtf8("text_sha"))

        self.retranslateUi(DexInfo)
        QtCore.QMetaObject.connectSlotsByName(DexInfo)

    def retranslateUi(self, DexInfo):
        DexInfo.setWindowTitle(_translate("DexInfo", "DexInformation", None))
        self.groupBox.setTitle(_translate("DexInfo", "DexInfo", None))
        self.lab_magic.setText(_translate("DexInfo", "Magic标识", None))
        self.lab_checksum.setText(_translate("DexInfo", "校验码", None))
        self.lab_dex_file_size.setText(_translate("DexInfo", "DEX文件大小", None))
        self.lab_header_size.setText(_translate("DexInfo", "文件头长度", None))
        self.lab_endian_tag.setText(_translate("DexInfo", "字节序标记", None))
        self.label_link_size.setText(_translate("DexInfo", "链接段大小", None))
        self.label_link_off.setText(_translate("DexInfo", "链接段基地址", None))
        self.label_map_off.setText(_translate("DexInfo", "Map数据基地址", None))
        self.label_string_ids_size.setText(_translate("DexInfo", "字符串列表的字符串数", None))
        self.label_string_ids_off.setText(_translate("DexInfo", "字符串列表表基地址", None))
        self.label_field_ids_size.setText(_translate("DexInfo", "字段列表里字段数", None))
        self.label_proto_ids_size.setText(_translate("DexInfo", "原型列表里原型数", None))
        self.label_method_ids_size.setText(_translate("DexInfo", "方法列表里方法数", None))
        self.label_field_ids_off.setText(_translate("DexInfo", "字段列表基地址", None))
        self.label_method_ids_off.setText(_translate("DexInfo", "方法列表基地址", None))
        self.label_data_size.setText(_translate("DexInfo", "数据段的大小", None))
        self.label_proto_ids_off.setText(_translate("DexInfo", "原型列表基地址", None))
        self.label_type_ids_off.setText(_translate("DexInfo", "类型列表基地址", None))
        self.label_class_defs_size.setText(_translate("DexInfo", "类定义类表中类的数", None))
        self.label_class_defs_off.setText(_translate("DexInfo", "类定义列表基地址", None))
        self.label_type_ids_size.setText(_translate("DexInfo", "类型列表中类型数", None))
        self.label_data_off.setText(_translate("DexInfo", "数据段基地址", None))
        self.label_sha.setText(_translate("DexInfo", "SHA-1签名", None))

