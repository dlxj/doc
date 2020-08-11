/********************************************************************************
** Form generated from reading UI file 'optiondialog.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_OPTIONDIALOG_H
#define UI_OPTIONDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include "browsefileedit.h"

QT_BEGIN_NAMESPACE

class Ui_OptionDialog
{
public:
    QVBoxLayout *verticalLayout;
    QTabWidget *tabWidget;
    QWidget *tab;
    QVBoxLayout *verticalLayout_2;
    QCheckBox *highlightCheck;
    QCheckBox *beepSoundCheck;
    QCheckBox *convertFullwidthCheck;
    QCheckBox *serverModeCheck;
    QFormLayout *formLayout;
    QLabel *label;
    QSpinBox *historyBox;
    QLabel *label_2;
    QSpinBox *indentOffsetBox;
    QLabel *label_3;
    QSpinBox *portNoBox;
    QWidget *tab_2;
    QFormLayout *formLayout_2;
    QLabel *label_4;
    BrowseFileEdit *waveProcEdit;
    QLabel *label_5;
    BrowseFileEdit *mpegProcEdit;
    BrowseFileEdit *browserProcEdit;
    QLineEdit *googleUrlEdit;
    QLabel *label_6;
    QLabel *label_7;
    QLineEdit *wikipediaUrlEdit;
    QLineEdit *userDefUrlEdit;
    QLabel *label_8;
    QLabel *label_9;
    QWidget *tab_3;
    QFormLayout *formLayout_3;
    QLabel *label_10;
    QSpinBox *limitCharBox;
    QLabel *label_11;
    QSpinBox *limitMenuBox;
    QLabel *label_12;
    QSpinBox *limitMaxBookBox;
    QLabel *label_13;
    QSpinBox *limitMaxTotalBox;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *OptionDialog)
    {
        if (OptionDialog->objectName().isEmpty())
            OptionDialog->setObjectName(QString::fromUtf8("OptionDialog"));
        OptionDialog->resize(467, 313);
        verticalLayout = new QVBoxLayout(OptionDialog);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        tabWidget = new QTabWidget(OptionDialog);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tab = new QWidget();
        tab->setObjectName(QString::fromUtf8("tab"));
        verticalLayout_2 = new QVBoxLayout(tab);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        highlightCheck = new QCheckBox(tab);
        highlightCheck->setObjectName(QString::fromUtf8("highlightCheck"));

        verticalLayout_2->addWidget(highlightCheck);

        beepSoundCheck = new QCheckBox(tab);
        beepSoundCheck->setObjectName(QString::fromUtf8("beepSoundCheck"));

        verticalLayout_2->addWidget(beepSoundCheck);

        convertFullwidthCheck = new QCheckBox(tab);
        convertFullwidthCheck->setObjectName(QString::fromUtf8("convertFullwidthCheck"));

        verticalLayout_2->addWidget(convertFullwidthCheck);

        serverModeCheck = new QCheckBox(tab);
        serverModeCheck->setObjectName(QString::fromUtf8("serverModeCheck"));

        verticalLayout_2->addWidget(serverModeCheck);

        formLayout = new QFormLayout();
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        label = new QLabel(tab);
        label->setObjectName(QString::fromUtf8("label"));

        formLayout->setWidget(1, QFormLayout::LabelRole, label);

        historyBox = new QSpinBox(tab);
        historyBox->setObjectName(QString::fromUtf8("historyBox"));
        historyBox->setMinimum(10);
        historyBox->setMaximum(1000);
        historyBox->setSingleStep(10);

        formLayout->setWidget(1, QFormLayout::FieldRole, historyBox);

        label_2 = new QLabel(tab);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        formLayout->setWidget(2, QFormLayout::LabelRole, label_2);

        indentOffsetBox = new QSpinBox(tab);
        indentOffsetBox->setObjectName(QString::fromUtf8("indentOffsetBox"));
        indentOffsetBox->setMaximum(100);
        indentOffsetBox->setSingleStep(10);

        formLayout->setWidget(2, QFormLayout::FieldRole, indentOffsetBox);

        label_3 = new QLabel(tab);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        formLayout->setWidget(3, QFormLayout::LabelRole, label_3);

        portNoBox = new QSpinBox(tab);
        portNoBox->setObjectName(QString::fromUtf8("portNoBox"));
        portNoBox->setMinimum(5000);
        portNoBox->setMaximum(9999);

        formLayout->setWidget(3, QFormLayout::FieldRole, portNoBox);


        verticalLayout_2->addLayout(formLayout);

        tabWidget->addTab(tab, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QString::fromUtf8("tab_2"));
        formLayout_2 = new QFormLayout(tab_2);
        formLayout_2->setObjectName(QString::fromUtf8("formLayout_2"));
        label_4 = new QLabel(tab_2);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        formLayout_2->setWidget(0, QFormLayout::LabelRole, label_4);

        waveProcEdit = new BrowseFileEdit(tab_2);
        waveProcEdit->setObjectName(QString::fromUtf8("waveProcEdit"));
        waveProcEdit->setFocusPolicy(Qt::StrongFocus);

        formLayout_2->setWidget(0, QFormLayout::FieldRole, waveProcEdit);

        label_5 = new QLabel(tab_2);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        formLayout_2->setWidget(1, QFormLayout::LabelRole, label_5);

        mpegProcEdit = new BrowseFileEdit(tab_2);
        mpegProcEdit->setObjectName(QString::fromUtf8("mpegProcEdit"));
        mpegProcEdit->setFocusPolicy(Qt::StrongFocus);

        formLayout_2->setWidget(1, QFormLayout::FieldRole, mpegProcEdit);

        browserProcEdit = new BrowseFileEdit(tab_2);
        browserProcEdit->setObjectName(QString::fromUtf8("browserProcEdit"));
        browserProcEdit->setFocusPolicy(Qt::StrongFocus);

        formLayout_2->setWidget(2, QFormLayout::FieldRole, browserProcEdit);

        googleUrlEdit = new QLineEdit(tab_2);
        googleUrlEdit->setObjectName(QString::fromUtf8("googleUrlEdit"));

        formLayout_2->setWidget(3, QFormLayout::FieldRole, googleUrlEdit);

        label_6 = new QLabel(tab_2);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        formLayout_2->setWidget(2, QFormLayout::LabelRole, label_6);

        label_7 = new QLabel(tab_2);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        formLayout_2->setWidget(3, QFormLayout::LabelRole, label_7);

        wikipediaUrlEdit = new QLineEdit(tab_2);
        wikipediaUrlEdit->setObjectName(QString::fromUtf8("wikipediaUrlEdit"));

        formLayout_2->setWidget(4, QFormLayout::FieldRole, wikipediaUrlEdit);

        userDefUrlEdit = new QLineEdit(tab_2);
        userDefUrlEdit->setObjectName(QString::fromUtf8("userDefUrlEdit"));

        formLayout_2->setWidget(5, QFormLayout::FieldRole, userDefUrlEdit);

        label_8 = new QLabel(tab_2);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        formLayout_2->setWidget(4, QFormLayout::LabelRole, label_8);

        label_9 = new QLabel(tab_2);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        formLayout_2->setWidget(5, QFormLayout::LabelRole, label_9);

        tabWidget->addTab(tab_2, QString());
        tab_3 = new QWidget();
        tab_3->setObjectName(QString::fromUtf8("tab_3"));
        formLayout_3 = new QFormLayout(tab_3);
        formLayout_3->setObjectName(QString::fromUtf8("formLayout_3"));
        label_10 = new QLabel(tab_3);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        formLayout_3->setWidget(0, QFormLayout::LabelRole, label_10);

        limitCharBox = new QSpinBox(tab_3);
        limitCharBox->setObjectName(QString::fromUtf8("limitCharBox"));
        limitCharBox->setMinimum(100000);
        limitCharBox->setMaximum(7000000);
        limitCharBox->setSingleStep(10000);

        formLayout_3->setWidget(0, QFormLayout::FieldRole, limitCharBox);

        label_11 = new QLabel(tab_3);
        label_11->setObjectName(QString::fromUtf8("label_11"));

        formLayout_3->setWidget(1, QFormLayout::LabelRole, label_11);

        limitMenuBox = new QSpinBox(tab_3);
        limitMenuBox->setObjectName(QString::fromUtf8("limitMenuBox"));
        limitMenuBox->setMinimum(100);
        limitMenuBox->setMaximum(7000);
        limitMenuBox->setSingleStep(100);

        formLayout_3->setWidget(1, QFormLayout::FieldRole, limitMenuBox);

        label_12 = new QLabel(tab_3);
        label_12->setObjectName(QString::fromUtf8("label_12"));

        formLayout_3->setWidget(2, QFormLayout::LabelRole, label_12);

        limitMaxBookBox = new QSpinBox(tab_3);
        limitMaxBookBox->setObjectName(QString::fromUtf8("limitMaxBookBox"));
        limitMaxBookBox->setMinimum(1000);
        limitMaxBookBox->setMaximum(100000);
        limitMaxBookBox->setSingleStep(1000);

        formLayout_3->setWidget(2, QFormLayout::FieldRole, limitMaxBookBox);

        label_13 = new QLabel(tab_3);
        label_13->setObjectName(QString::fromUtf8("label_13"));

        formLayout_3->setWidget(3, QFormLayout::LabelRole, label_13);

        limitMaxTotalBox = new QSpinBox(tab_3);
        limitMaxTotalBox->setObjectName(QString::fromUtf8("limitMaxTotalBox"));
        limitMaxTotalBox->setMinimum(1000);
        limitMaxTotalBox->setMaximum(100000);
        limitMaxTotalBox->setSingleStep(1000);

        formLayout_3->setWidget(3, QFormLayout::FieldRole, limitMaxTotalBox);

        tabWidget->addTab(tab_3, QString());

        verticalLayout->addWidget(tabWidget);

        buttonBox = new QDialogButtonBox(OptionDialog);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);

        QWidget::setTabOrder(tabWidget, highlightCheck);
        QWidget::setTabOrder(highlightCheck, beepSoundCheck);
        QWidget::setTabOrder(beepSoundCheck, convertFullwidthCheck);
        QWidget::setTabOrder(convertFullwidthCheck, serverModeCheck);
        QWidget::setTabOrder(serverModeCheck, historyBox);
        QWidget::setTabOrder(historyBox, indentOffsetBox);
        QWidget::setTabOrder(indentOffsetBox, portNoBox);
        QWidget::setTabOrder(portNoBox, waveProcEdit);
        QWidget::setTabOrder(waveProcEdit, mpegProcEdit);
        QWidget::setTabOrder(mpegProcEdit, browserProcEdit);
        QWidget::setTabOrder(browserProcEdit, googleUrlEdit);
        QWidget::setTabOrder(googleUrlEdit, wikipediaUrlEdit);
        QWidget::setTabOrder(wikipediaUrlEdit, userDefUrlEdit);
        QWidget::setTabOrder(userDefUrlEdit, limitCharBox);
        QWidget::setTabOrder(limitCharBox, limitMenuBox);
        QWidget::setTabOrder(limitMenuBox, limitMaxBookBox);
        QWidget::setTabOrder(limitMaxBookBox, limitMaxTotalBox);

        retranslateUi(OptionDialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), OptionDialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), OptionDialog, SLOT(reject()));

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(OptionDialog);
    } // setupUi

    void retranslateUi(QDialog *OptionDialog)
    {
        OptionDialog->setWindowTitle(QCoreApplication::translate("OptionDialog", "Options", nullptr));
        highlightCheck->setText(QCoreApplication::translate("OptionDialog", "Emphasize match string", nullptr));
        beepSoundCheck->setText(QCoreApplication::translate("OptionDialog", "Beep sound", nullptr));
        convertFullwidthCheck->setText(QCoreApplication::translate("OptionDialog", "Convert Fullwidth to Halfwidth characters in book titles", nullptr));
        serverModeCheck->setText(QCoreApplication::translate("OptionDialog", "Server mode(must restart)", nullptr));
        label->setText(QCoreApplication::translate("OptionDialog", "Max history", nullptr));
        label_2->setText(QCoreApplication::translate("OptionDialog", "Indent offset", nullptr));
        label_3->setText(QCoreApplication::translate("OptionDialog", "Port No (server mode)", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab), QCoreApplication::translate("OptionDialog", "General", nullptr));
        label_4->setText(QCoreApplication::translate("OptionDialog", "Sound(wave)", nullptr));
        label_5->setText(QCoreApplication::translate("OptionDialog", "Movie(mpeg)", nullptr));
        label_6->setText(QCoreApplication::translate("OptionDialog", "Web browser", nullptr));
        label_7->setText(QCoreApplication::translate("OptionDialog", "Google URL", nullptr));
        label_8->setText(QCoreApplication::translate("OptionDialog", "Wikipedia URL", nullptr));
        label_9->setText(QCoreApplication::translate("OptionDialog", "User defined URL", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QCoreApplication::translate("OptionDialog", "External program", nullptr));
        label_10->setText(QCoreApplication::translate("OptionDialog", "Limit of characters", nullptr));
        label_11->setText(QCoreApplication::translate("OptionDialog", "Limit of menu items", nullptr));
        label_12->setText(QCoreApplication::translate("OptionDialog", "Limit of hits per book", nullptr));
        label_13->setText(QCoreApplication::translate("OptionDialog", "Limit of total hits", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_3), QCoreApplication::translate("OptionDialog", "Advanced", nullptr));
    } // retranslateUi

};

namespace Ui {
    class OptionDialog: public Ui_OptionDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_OPTIONDIALOG_H
