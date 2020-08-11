/********************************************************************************
** Form generated from reading UI file 'clipboardoptionswidget.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CLIPBOARDOPTIONSWIDGET_H
#define UI_CLIPBOARDOPTIONSWIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_ClipboardOptionsWidget
{
public:
    QVBoxLayout *verticalLayout;
    QGroupBox *gb;
    QVBoxLayout *verticalLayout_3;
    QRadioButton *clipboardRadio;
    QStackedWidget *stackedWidget;
    QWidget *selectionPage;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *hl1;
    QRadioButton *selectionRadio;
    QLabel *l1;
    QSpinBox *selectionDelayBox;
    QLabel *l2;
    QSpacerItem *hs;
    QCheckBox *raiseWindowCheck;
    QSpacerItem *v1;
    QWidget *findBufferPage;
    QGridLayout *gridLayout;
    QRadioButton *findBufferRadio;
    QSpacerItem *v2;
    QButtonGroup *buttonGroup;

    void setupUi(QWidget *ClipboardOptionsWidget)
    {
        if (ClipboardOptionsWidget->objectName().isEmpty())
            ClipboardOptionsWidget->setObjectName(QString::fromUtf8("ClipboardOptionsWidget"));
        ClipboardOptionsWidget->resize(400, 300);
        verticalLayout = new QVBoxLayout(ClipboardOptionsWidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(9, -1, -1, -1);
        gb = new QGroupBox(ClipboardOptionsWidget);
        gb->setObjectName(QString::fromUtf8("gb"));
        verticalLayout_3 = new QVBoxLayout(gb);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        clipboardRadio = new QRadioButton(gb);
        buttonGroup = new QButtonGroup(ClipboardOptionsWidget);
        buttonGroup->setObjectName(QString::fromUtf8("buttonGroup"));
        buttonGroup->addButton(clipboardRadio);
        clipboardRadio->setObjectName(QString::fromUtf8("clipboardRadio"));
        clipboardRadio->setChecked(true);

        verticalLayout_3->addWidget(clipboardRadio);

        stackedWidget = new QStackedWidget(gb);
        stackedWidget->setObjectName(QString::fromUtf8("stackedWidget"));
        selectionPage = new QWidget();
        selectionPage->setObjectName(QString::fromUtf8("selectionPage"));
        verticalLayout_2 = new QVBoxLayout(selectionPage);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        hl1 = new QHBoxLayout();
        hl1->setObjectName(QString::fromUtf8("hl1"));
        selectionRadio = new QRadioButton(selectionPage);
        buttonGroup->addButton(selectionRadio);
        selectionRadio->setObjectName(QString::fromUtf8("selectionRadio"));

        hl1->addWidget(selectionRadio);

        l1 = new QLabel(selectionPage);
        l1->setObjectName(QString::fromUtf8("l1"));
        l1->setEnabled(false);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(l1->sizePolicy().hasHeightForWidth());
        l1->setSizePolicy(sizePolicy);

        hl1->addWidget(l1);

        selectionDelayBox = new QSpinBox(selectionPage);
        selectionDelayBox->setObjectName(QString::fromUtf8("selectionDelayBox"));
        selectionDelayBox->setEnabled(false);
        selectionDelayBox->setAccelerated(true);
        selectionDelayBox->setMaximum(5000);
        selectionDelayBox->setSingleStep(100);

        hl1->addWidget(selectionDelayBox);

        l2 = new QLabel(selectionPage);
        l2->setObjectName(QString::fromUtf8("l2"));
        l2->setEnabled(false);
        sizePolicy.setHeightForWidth(l2->sizePolicy().hasHeightForWidth());
        l2->setSizePolicy(sizePolicy);

        hl1->addWidget(l2);

        hs = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        hl1->addItem(hs);


        verticalLayout_2->addLayout(hl1);

        raiseWindowCheck = new QCheckBox(selectionPage);
        raiseWindowCheck->setObjectName(QString::fromUtf8("raiseWindowCheck"));

        verticalLayout_2->addWidget(raiseWindowCheck);

        v1 = new QSpacerItem(20, 147, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(v1);

        stackedWidget->addWidget(selectionPage);
        findBufferPage = new QWidget();
        findBufferPage->setObjectName(QString::fromUtf8("findBufferPage"));
        gridLayout = new QGridLayout(findBufferPage);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        findBufferRadio = new QRadioButton(findBufferPage);
        buttonGroup->addButton(findBufferRadio);
        findBufferRadio->setObjectName(QString::fromUtf8("findBufferRadio"));

        gridLayout->addWidget(findBufferRadio, 0, 0, 1, 1);

        v2 = new QSpacerItem(20, 195, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(v2, 1, 0, 1, 1);

        stackedWidget->addWidget(findBufferPage);

        verticalLayout_3->addWidget(stackedWidget);


        verticalLayout->addWidget(gb);


        retranslateUi(ClipboardOptionsWidget);
        QObject::connect(selectionRadio, SIGNAL(toggled(bool)), selectionDelayBox, SLOT(setEnabled(bool)));
        QObject::connect(selectionRadio, SIGNAL(toggled(bool)), l2, SLOT(setEnabled(bool)));
        QObject::connect(selectionRadio, SIGNAL(toggled(bool)), l1, SLOT(setEnabled(bool)));

        stackedWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(ClipboardOptionsWidget);
    } // setupUi

    void retranslateUi(QWidget *ClipboardOptionsWidget)
    {
        ClipboardOptionsWidget->setWindowTitle(QCoreApplication::translate("ClipboardOptionsWidget", "Form", nullptr));
        gb->setTitle(QCoreApplication::translate("ClipboardOptionsWidget", "\"Watch clipboard\" mode", nullptr));
        clipboardRadio->setText(QCoreApplication::translate("ClipboardOptionsWidget", "&Clipboard", nullptr));
        selectionRadio->setText(QCoreApplication::translate("ClipboardOptionsWidget", "&Primary selection", nullptr));
        l1->setText(QCoreApplication::translate("ClipboardOptionsWidget", "after", nullptr));
        l2->setText(QCoreApplication::translate("ClipboardOptionsWidget", "milliseconds", nullptr));
        raiseWindowCheck->setText(QCoreApplication::translate("ClipboardOptionsWidget", "&Raise application window", nullptr));
        findBufferRadio->setText(QCoreApplication::translate("ClipboardOptionsWidget", "&Find buffer", nullptr));
    } // retranslateUi

};

namespace Ui {
    class ClipboardOptionsWidget: public Ui_ClipboardOptionsWidget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CLIPBOARDOPTIONSWIDGET_H
