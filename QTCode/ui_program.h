/********************************************************************************
** Form generated from reading UI file 'programlx3073.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef PROGRAMLX3073_H
#define PROGRAMLX3073_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QComboBox>
#include <QtGui/QFrame>
#include <QtGui/QGridLayout>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QListWidget>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QPushButton>
#include <QtGui/QSlider>
#include <QtGui/QSpacerItem>
#include <QtGui/QSpinBox>
#include <QtGui/QStatusBar>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QGridLayout *gridLayout_6;
    QFrame *framesearch;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout;
    QSpinBox *IDMAX;
    QLabel *label_5;
    QSpinBox *IDMIN;
    QLabel *label_4;
    QLabel *portttxt;
    QComboBox *portcombox;
    QLabel *BAUDRATEtxt;
    QHBoxLayout *horizontalLayout_5;
    QSpacerItem *horizontalSpacer;
    QPushButton *scanbutton;
    QSpacerItem *horizontalSpacer_2;
    QListWidget *Baudratelist;
    QHBoxLayout *horizontalLayout_8;
    QSpacerItem *horizontalSpacer_3;
    QLabel *searchparamtxt;
    QSpacerItem *horizontalSpacer_4;
    QFrame *framelist;
    QGridLayout *gridLayout_2;
    QLabel *label_6;
    QListWidget *listWidget;
    QVBoxLayout *verticalLayout_7;
    QFrame *frameconfig;
    QGridLayout *gridLayout_7;
    QComboBox *modellist;
    QHBoxLayout *horizontalLayout_2;
    QLabel *torquemaxtxt;
    QSlider *torqueslider;
    QHBoxLayout *horizontalLayout_4;
    QSpinBox *spinBox;
    QLabel *label;
    QHBoxLayout *horizontalLayout_7;
    QCheckBox *reversemode_2;
    QCheckBox *slavemode_2;
    QLabel *label_7;
    QGridLayout *gridLayout_3;
    QVBoxLayout *verticalLayout;
    QLabel *servoidtxt;
    QSpinBox *servoid;
    QVBoxLayout *verticalLayout_2;
    QLabel *servobaudrate;
    QComboBox *servobaudlist;
    QCheckBox *checkBox;
    QVBoxLayout *verticalLayout_3;
    QLabel *newidtxt;
    QSpinBox *newid;
    QVBoxLayout *verticalLayout_4;
    QLabel *newbaud;
    QComboBox *newbaudlist;
    QPushButton *updatememory;
    QGridLayout *gridLayout_5;
    QLabel *label_16;
    QHBoxLayout *horizontalLayout_6;
    QCheckBox *wheel_2;
    QCheckBox *joint_2;
    QCheckBox *multiturn_2;
    QGridLayout *gridLayout_4;
    QVBoxLayout *verticalLayout_6;
    QLabel *label_13;
    QSpinBox *cwanglelimit;
    QVBoxLayout *verticalLayout_5;
    QLabel *label_14;
    QSpinBox *ccwanglelimit;
    QLabel *label_2;
    QVBoxLayout *verticalLayout_8;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_3;
    QLabel *label_8;
    QLabel *label_9;
    QHBoxLayout *horizontalLayout_9;
    QSpinBox *Dgain;
    QSpinBox *Igain;
    QSpinBox *pgain;
    QSpacerItem *verticalSpacer;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(887, 587);
        MainWindow->setMinimumSize(QSize(887, 587));
        MainWindow->setStyleSheet(QString::fromUtf8(""));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout_6 = new QGridLayout(centralwidget);
        gridLayout_6->setObjectName(QString::fromUtf8("gridLayout_6"));
        framesearch = new QFrame(centralwidget);
        framesearch->setObjectName(QString::fromUtf8("framesearch"));
        framesearch->setFrameShape(QFrame::NoFrame);
        framesearch->setFrameShadow(QFrame::Raised);
        gridLayout = new QGridLayout(framesearch);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        IDMAX = new QSpinBox(framesearch);
        IDMAX->setObjectName(QString::fromUtf8("IDMAX"));
        IDMAX->setAccelerated(true);
        IDMAX->setMinimum(1);
        IDMAX->setMaximum(252);
        IDMAX->setSingleStep(1);

        horizontalLayout->addWidget(IDMAX);

        label_5 = new QLabel(framesearch);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        horizontalLayout->addWidget(label_5);

        IDMIN = new QSpinBox(framesearch);
        IDMIN->setObjectName(QString::fromUtf8("IDMIN"));
        IDMIN->setAccelerated(true);
        IDMIN->setMinimum(1);
        IDMIN->setMaximum(252);

        horizontalLayout->addWidget(IDMIN);

        label_4 = new QLabel(framesearch);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        horizontalLayout->addWidget(label_4);


        gridLayout->addLayout(horizontalLayout, 5, 0, 1, 1);

        portttxt = new QLabel(framesearch);
        portttxt->setObjectName(QString::fromUtf8("portttxt"));

        gridLayout->addWidget(portttxt, 1, 0, 1, 1);

        portcombox = new QComboBox(framesearch);
        portcombox->setObjectName(QString::fromUtf8("portcombox"));

        gridLayout->addWidget(portcombox, 2, 0, 1, 1);

        BAUDRATEtxt = new QLabel(framesearch);
        BAUDRATEtxt->setObjectName(QString::fromUtf8("BAUDRATEtxt"));

        gridLayout->addWidget(BAUDRATEtxt, 3, 0, 1, 1);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer);

        scanbutton = new QPushButton(framesearch);
        scanbutton->setObjectName(QString::fromUtf8("scanbutton"));
        scanbutton->setMinimumSize(QSize(266, 27));
        scanbutton->setMaximumSize(QSize(266, 27));
        scanbutton->setLayoutDirection(Qt::LeftToRight);
        scanbutton->setStyleSheet(QString::fromUtf8("background-image: url(:/testebutton.jpg);"));

        horizontalLayout_5->addWidget(scanbutton);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_2);


        gridLayout->addLayout(horizontalLayout_5, 6, 0, 1, 1);

        Baudratelist = new QListWidget(framesearch);
        QListWidgetItem *__qlistwidgetitem = new QListWidgetItem(Baudratelist);
        __qlistwidgetitem->setCheckState(Qt::Unchecked);
        QListWidgetItem *__qlistwidgetitem1 = new QListWidgetItem(Baudratelist);
        __qlistwidgetitem1->setCheckState(Qt::Unchecked);
        QListWidgetItem *__qlistwidgetitem2 = new QListWidgetItem(Baudratelist);
        __qlistwidgetitem2->setCheckState(Qt::Unchecked);
        QListWidgetItem *__qlistwidgetitem3 = new QListWidgetItem(Baudratelist);
        __qlistwidgetitem3->setCheckState(Qt::Unchecked);
        QListWidgetItem *__qlistwidgetitem4 = new QListWidgetItem(Baudratelist);
        __qlistwidgetitem4->setCheckState(Qt::Unchecked);
        QListWidgetItem *__qlistwidgetitem5 = new QListWidgetItem(Baudratelist);
        __qlistwidgetitem5->setCheckState(Qt::Unchecked);
        QListWidgetItem *__qlistwidgetitem6 = new QListWidgetItem(Baudratelist);
        __qlistwidgetitem6->setCheckState(Qt::Unchecked);
        QListWidgetItem *__qlistwidgetitem7 = new QListWidgetItem(Baudratelist);
        __qlistwidgetitem7->setCheckState(Qt::Unchecked);
        QListWidgetItem *__qlistwidgetitem8 = new QListWidgetItem(Baudratelist);
        __qlistwidgetitem8->setCheckState(Qt::Unchecked);
        Baudratelist->setObjectName(QString::fromUtf8("Baudratelist"));
        Baudratelist->setFrameShape(QFrame::StyledPanel);
        Baudratelist->setFrameShadow(QFrame::Sunken);
        Baudratelist->setLineWidth(0);
        Baudratelist->setMidLineWidth(0);
        Baudratelist->setVerticalScrollBarPolicy(Qt::ScrollBarAsNeeded);
        Baudratelist->setDragEnabled(false);
        Baudratelist->setDragDropOverwriteMode(false);
        Baudratelist->setMovement(QListView::Static);
        Baudratelist->setFlow(QListView::TopToBottom);
        Baudratelist->setViewMode(QListView::ListMode);
        Baudratelist->setUniformItemSizes(false);
        Baudratelist->setWordWrap(false);
        Baudratelist->setSortingEnabled(false);

        gridLayout->addWidget(Baudratelist, 4, 0, 1, 1);

        horizontalLayout_8 = new QHBoxLayout();
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_8->addItem(horizontalSpacer_3);

        searchparamtxt = new QLabel(framesearch);
        searchparamtxt->setObjectName(QString::fromUtf8("searchparamtxt"));

        horizontalLayout_8->addWidget(searchparamtxt);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_8->addItem(horizontalSpacer_4);


        gridLayout->addLayout(horizontalLayout_8, 0, 0, 1, 1);


        gridLayout_6->addWidget(framesearch, 0, 0, 1, 1);

        framelist = new QFrame(centralwidget);
        framelist->setObjectName(QString::fromUtf8("framelist"));
        framelist->setFrameShape(QFrame::NoFrame);
        framelist->setFrameShadow(QFrame::Raised);
        gridLayout_2 = new QGridLayout(framelist);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label_6 = new QLabel(framelist);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setEnabled(true);
        label_6->setLayoutDirection(Qt::LeftToRight);
        label_6->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_6, 0, 0, 1, 1);

        listWidget = new QListWidget(framelist);
        listWidget->setObjectName(QString::fromUtf8("listWidget"));
        listWidget->setAutoFillBackground(false);
        listWidget->setFrameShape(QFrame::Panel);

        gridLayout_2->addWidget(listWidget, 1, 0, 1, 1);


        gridLayout_6->addWidget(framelist, 0, 1, 1, 1);

        verticalLayout_7 = new QVBoxLayout();
        verticalLayout_7->setObjectName(QString::fromUtf8("verticalLayout_7"));
        frameconfig = new QFrame(centralwidget);
        frameconfig->setObjectName(QString::fromUtf8("frameconfig"));
        frameconfig->setMaximumSize(QSize(273, 523));
        frameconfig->setFrameShape(QFrame::NoFrame);
        frameconfig->setFrameShadow(QFrame::Raised);
        gridLayout_7 = new QGridLayout(frameconfig);
        gridLayout_7->setObjectName(QString::fromUtf8("gridLayout_7"));
        modellist = new QComboBox(frameconfig);
        modellist->setObjectName(QString::fromUtf8("modellist"));

        gridLayout_7->addWidget(modellist, 2, 0, 1, 1);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        torquemaxtxt = new QLabel(frameconfig);
        torquemaxtxt->setObjectName(QString::fromUtf8("torquemaxtxt"));

        horizontalLayout_2->addWidget(torquemaxtxt);

        torqueslider = new QSlider(frameconfig);
        torqueslider->setObjectName(QString::fromUtf8("torqueslider"));
        torqueslider->setMinimum(1);
        torqueslider->setMaximum(100);
        torqueslider->setValue(100);
        torqueslider->setTracking(true);
        torqueslider->setOrientation(Qt::Horizontal);

        horizontalLayout_2->addWidget(torqueslider);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        spinBox = new QSpinBox(frameconfig);
        spinBox->setObjectName(QString::fromUtf8("spinBox"));
        spinBox->setMinimum(1);
        spinBox->setMaximum(100);
        spinBox->setValue(100);

        horizontalLayout_4->addWidget(spinBox);

        label = new QLabel(frameconfig);
        label->setObjectName(QString::fromUtf8("label"));
        label->setAlignment(Qt::AlignCenter);

        horizontalLayout_4->addWidget(label);


        horizontalLayout_2->addLayout(horizontalLayout_4);


        gridLayout_7->addLayout(horizontalLayout_2, 4, 0, 1, 1);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        reversemode_2 = new QCheckBox(frameconfig);
        reversemode_2->setObjectName(QString::fromUtf8("reversemode_2"));
        reversemode_2->setEnabled(false);

        horizontalLayout_7->addWidget(reversemode_2);

        slavemode_2 = new QCheckBox(frameconfig);
        slavemode_2->setObjectName(QString::fromUtf8("slavemode_2"));
        slavemode_2->setEnabled(false);

        horizontalLayout_7->addWidget(slavemode_2);


        gridLayout_7->addLayout(horizontalLayout_7, 8, 0, 1, 1);

        label_7 = new QLabel(frameconfig);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setAlignment(Qt::AlignCenter);

        gridLayout_7->addWidget(label_7, 0, 0, 1, 1);

        gridLayout_3 = new QGridLayout();
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        servoidtxt = new QLabel(frameconfig);
        servoidtxt->setObjectName(QString::fromUtf8("servoidtxt"));

        verticalLayout->addWidget(servoidtxt);

        servoid = new QSpinBox(frameconfig);
        servoid->setObjectName(QString::fromUtf8("servoid"));
        servoid->setAccelerated(true);
        servoid->setMinimum(1);
        servoid->setMaximum(252);

        verticalLayout->addWidget(servoid);


        gridLayout_3->addLayout(verticalLayout, 0, 0, 1, 1);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        servobaudrate = new QLabel(frameconfig);
        servobaudrate->setObjectName(QString::fromUtf8("servobaudrate"));

        verticalLayout_2->addWidget(servobaudrate);

        servobaudlist = new QComboBox(frameconfig);
        servobaudlist->setObjectName(QString::fromUtf8("servobaudlist"));

        verticalLayout_2->addWidget(servobaudlist);


        gridLayout_3->addLayout(verticalLayout_2, 0, 1, 1, 2);

        checkBox = new QCheckBox(frameconfig);
        checkBox->setObjectName(QString::fromUtf8("checkBox"));

        gridLayout_3->addWidget(checkBox, 1, 0, 1, 2);

        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        newidtxt = new QLabel(frameconfig);
        newidtxt->setObjectName(QString::fromUtf8("newidtxt"));

        verticalLayout_3->addWidget(newidtxt);

        newid = new QSpinBox(frameconfig);
        newid->setObjectName(QString::fromUtf8("newid"));
        newid->setAccelerated(true);
        newid->setMinimum(1);
        newid->setMaximum(252);

        verticalLayout_3->addWidget(newid);


        gridLayout_3->addLayout(verticalLayout_3, 2, 0, 1, 1);

        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        newbaud = new QLabel(frameconfig);
        newbaud->setObjectName(QString::fromUtf8("newbaud"));

        verticalLayout_4->addWidget(newbaud);

        newbaudlist = new QComboBox(frameconfig);
        newbaudlist->setObjectName(QString::fromUtf8("newbaudlist"));

        verticalLayout_4->addWidget(newbaudlist);


        gridLayout_3->addLayout(verticalLayout_4, 2, 2, 1, 1);


        gridLayout_7->addLayout(gridLayout_3, 3, 0, 1, 1);

        updatememory = new QPushButton(frameconfig);
        updatememory->setObjectName(QString::fromUtf8("updatememory"));
        updatememory->setMaximumSize(QSize(1920, 1080));
        updatememory->setStyleSheet(QString::fromUtf8("background-image: url(:/updateeprombut.jpg);"));
        updatememory->setFlat(false);

        gridLayout_7->addWidget(updatememory, 9, 0, 1, 1);

        gridLayout_5 = new QGridLayout();
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        label_16 = new QLabel(frameconfig);
        label_16->setObjectName(QString::fromUtf8("label_16"));
        label_16->setAlignment(Qt::AlignCenter);

        gridLayout_5->addWidget(label_16, 0, 0, 1, 1);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        wheel_2 = new QCheckBox(frameconfig);
        wheel_2->setObjectName(QString::fromUtf8("wheel_2"));
        wheel_2->setStyleSheet(QString::fromUtf8("background-image: url(:/background.jpg);"));

        horizontalLayout_6->addWidget(wheel_2);

        joint_2 = new QCheckBox(frameconfig);
        joint_2->setObjectName(QString::fromUtf8("joint_2"));
        joint_2->setAutoFillBackground(false);
        joint_2->setCheckable(true);
        joint_2->setTristate(false);

        horizontalLayout_6->addWidget(joint_2);

        multiturn_2 = new QCheckBox(frameconfig);
        multiturn_2->setObjectName(QString::fromUtf8("multiturn_2"));
        multiturn_2->setEnabled(false);

        horizontalLayout_6->addWidget(multiturn_2);


        gridLayout_5->addLayout(horizontalLayout_6, 1, 0, 1, 1);

        gridLayout_4 = new QGridLayout();
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        verticalLayout_6 = new QVBoxLayout();
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        label_13 = new QLabel(frameconfig);
        label_13->setObjectName(QString::fromUtf8("label_13"));

        verticalLayout_6->addWidget(label_13);

        cwanglelimit = new QSpinBox(frameconfig);
        cwanglelimit->setObjectName(QString::fromUtf8("cwanglelimit"));
        cwanglelimit->setEnabled(false);
        cwanglelimit->setFrame(true);
        cwanglelimit->setAccelerated(true);
        cwanglelimit->setKeyboardTracking(true);
        cwanglelimit->setSuffix(QString::fromUtf8(""));
        cwanglelimit->setMaximum(4095);

        verticalLayout_6->addWidget(cwanglelimit);


        gridLayout_4->addLayout(verticalLayout_6, 0, 0, 1, 1);

        verticalLayout_5 = new QVBoxLayout();
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        label_14 = new QLabel(frameconfig);
        label_14->setObjectName(QString::fromUtf8("label_14"));

        verticalLayout_5->addWidget(label_14);

        ccwanglelimit = new QSpinBox(frameconfig);
        ccwanglelimit->setObjectName(QString::fromUtf8("ccwanglelimit"));
        ccwanglelimit->setEnabled(false);
        ccwanglelimit->setAccelerated(true);
        ccwanglelimit->setMaximum(4095);

        verticalLayout_5->addWidget(ccwanglelimit);


        gridLayout_4->addLayout(verticalLayout_5, 0, 1, 1, 1);


        gridLayout_5->addLayout(gridLayout_4, 2, 0, 1, 1);


        gridLayout_7->addLayout(gridLayout_5, 6, 0, 1, 1);

        label_2 = new QLabel(frameconfig);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout_7->addWidget(label_2, 1, 0, 1, 1);

        verticalLayout_8 = new QVBoxLayout();
        verticalLayout_8->setObjectName(QString::fromUtf8("verticalLayout_8"));
        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_3 = new QLabel(frameconfig);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        horizontalLayout_3->addWidget(label_3);

        label_8 = new QLabel(frameconfig);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        horizontalLayout_3->addWidget(label_8);

        label_9 = new QLabel(frameconfig);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        horizontalLayout_3->addWidget(label_9);


        verticalLayout_8->addLayout(horizontalLayout_3);

        horizontalLayout_9 = new QHBoxLayout();
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        Dgain = new QSpinBox(frameconfig);
        Dgain->setObjectName(QString::fromUtf8("Dgain"));
        Dgain->setAccelerated(true);
        Dgain->setMaximum(254);

        horizontalLayout_9->addWidget(Dgain);

        Igain = new QSpinBox(frameconfig);
        Igain->setObjectName(QString::fromUtf8("Igain"));
        Igain->setAccelerated(true);
        Igain->setMaximum(254);

        horizontalLayout_9->addWidget(Igain);

        pgain = new QSpinBox(frameconfig);
        pgain->setObjectName(QString::fromUtf8("pgain"));
        pgain->setAccelerated(true);
        pgain->setMaximum(254);
        pgain->setValue(10);

        horizontalLayout_9->addWidget(pgain);


        verticalLayout_8->addLayout(horizontalLayout_9);


        gridLayout_7->addLayout(verticalLayout_8, 7, 0, 1, 1);


        verticalLayout_7->addWidget(frameconfig);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_7->addItem(verticalSpacer);


        gridLayout_6->addLayout(verticalLayout_7, 0, 2, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 887, 25));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);
        QObject::connect(torqueslider, SIGNAL(sliderMoved(int)), spinBox, SLOT(setValue(int)));
        QObject::connect(spinBox, SIGNAL(valueChanged(int)), torqueslider, SLOT(setValue(int)));
        QObject::connect(joint_2, SIGNAL(clicked(bool)), ccwanglelimit, SLOT(setEnabled(bool)));
        QObject::connect(joint_2, SIGNAL(clicked(bool)), cwanglelimit, SLOT(setEnabled(bool)));

        Baudratelist->setCurrentRow(-1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("MainWindow", "Max. ID", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("MainWindow", "Min. ID", 0, QApplication::UnicodeUTF8));
        portttxt->setText(QApplication::translate("MainWindow", "PORTS", 0, QApplication::UnicodeUTF8));
        portcombox->clear();
        portcombox->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "/dev/ttyUSB0", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "/dev/ttyUSB1", 0, QApplication::UnicodeUTF8)
        );
        BAUDRATEtxt->setText(QApplication::translate("MainWindow", "BAUDRATES", 0, QApplication::UnicodeUTF8));
        scanbutton->setText(QApplication::translate("MainWindow", "SCAN", 0, QApplication::UnicodeUTF8));

        const bool __sortingEnabled = Baudratelist->isSortingEnabled();
        Baudratelist->setSortingEnabled(false);
        QListWidgetItem *___qlistwidgetitem = Baudratelist->item(0);
        ___qlistwidgetitem->setText(QApplication::translate("MainWindow", "1000000", 0, QApplication::UnicodeUTF8));
        QListWidgetItem *___qlistwidgetitem1 = Baudratelist->item(1);
        ___qlistwidgetitem1->setText(QApplication::translate("MainWindow", "500000", 0, QApplication::UnicodeUTF8));
        QListWidgetItem *___qlistwidgetitem2 = Baudratelist->item(2);
        ___qlistwidgetitem2->setText(QApplication::translate("MainWindow", "400000", 0, QApplication::UnicodeUTF8));
        QListWidgetItem *___qlistwidgetitem3 = Baudratelist->item(3);
        ___qlistwidgetitem3->setText(QApplication::translate("MainWindow", "250000", 0, QApplication::UnicodeUTF8));
        QListWidgetItem *___qlistwidgetitem4 = Baudratelist->item(4);
        ___qlistwidgetitem4->setText(QApplication::translate("MainWindow", "200000", 0, QApplication::UnicodeUTF8));
        QListWidgetItem *___qlistwidgetitem5 = Baudratelist->item(5);
        ___qlistwidgetitem5->setText(QApplication::translate("MainWindow", "115200", 0, QApplication::UnicodeUTF8));
        QListWidgetItem *___qlistwidgetitem6 = Baudratelist->item(6);
        ___qlistwidgetitem6->setText(QApplication::translate("MainWindow", "57600", 0, QApplication::UnicodeUTF8));
        QListWidgetItem *___qlistwidgetitem7 = Baudratelist->item(7);
        ___qlistwidgetitem7->setText(QApplication::translate("MainWindow", "19200", 0, QApplication::UnicodeUTF8));
        QListWidgetItem *___qlistwidgetitem8 = Baudratelist->item(8);
        ___qlistwidgetitem8->setText(QApplication::translate("MainWindow", "9600", 0, QApplication::UnicodeUTF8));
        Baudratelist->setSortingEnabled(__sortingEnabled);

        searchparamtxt->setText(QApplication::translate("MainWindow", "SEARCH PARAMETERS", 0, QApplication::UnicodeUTF8));
        label_6->setText(QApplication::translate("MainWindow", "Motors Found", 0, QApplication::UnicodeUTF8));
        modellist->clear();
        modellist->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "AX-12Wnomulti", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "AX-12Anomulti", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "AX-18nomulti", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "EX-106+ nomulti", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "RX-24F nomulti", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "RX-28 nomulti", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "RX-64 nomulti", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "MX-12W ", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "MX-28", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "MX-64", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "MX-106drive", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "MX1062.0 NON SUPORTED", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "MX-28 2.0 NON SUPORTED", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "MX-64 2.0 NON SUPORTED", 0, QApplication::UnicodeUTF8)
        );
        torquemaxtxt->setText(QApplication::translate("MainWindow", "Torque Max", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MainWindow", "%", 0, QApplication::UnicodeUTF8));
        reversemode_2->setText(QApplication::translate("MainWindow", "Reverse Mode", 0, QApplication::UnicodeUTF8));
        slavemode_2->setText(QApplication::translate("MainWindow", "Slave Mode", 0, QApplication::UnicodeUTF8));
        label_7->setText(QApplication::translate("MainWindow", "Configuration Parameters", 0, QApplication::UnicodeUTF8));
        servoidtxt->setText(QApplication::translate("MainWindow", "Servo ID", 0, QApplication::UnicodeUTF8));
        servobaudrate->setText(QApplication::translate("MainWindow", "Servo Baudrate", 0, QApplication::UnicodeUTF8));
        servobaudlist->clear();
        servobaudlist->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "1000000", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "500000", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "400000", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "250000", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "200000", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "11520", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "57600", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "19200", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "9600", 0, QApplication::UnicodeUTF8)
        );
        checkBox->setText(QApplication::translate("MainWindow", "Factory Reset", 0, QApplication::UnicodeUTF8));
        newidtxt->setText(QApplication::translate("MainWindow", "New ID", 0, QApplication::UnicodeUTF8));
        newbaud->setText(QApplication::translate("MainWindow", "New Baudrate", 0, QApplication::UnicodeUTF8));
        newbaudlist->clear();
        newbaudlist->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "1000000", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "500000", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "400000", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "250000", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "200000", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "11520", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "57600", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "19200", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "9600", 0, QApplication::UnicodeUTF8)
        );
        updatememory->setText(QApplication::translate("MainWindow", "UPDATE MEMORY", 0, QApplication::UnicodeUTF8));
        label_16->setText(QApplication::translate("MainWindow", "Mode set", 0, QApplication::UnicodeUTF8));
        wheel_2->setText(QApplication::translate("MainWindow", "Wheel", 0, QApplication::UnicodeUTF8));
        joint_2->setText(QApplication::translate("MainWindow", "Joint", 0, QApplication::UnicodeUTF8));
        multiturn_2->setText(QApplication::translate("MainWindow", "Multi Turn", 0, QApplication::UnicodeUTF8));
        label_13->setText(QApplication::translate("MainWindow", "CW ANGLE LIMIT", 0, QApplication::UnicodeUTF8));
        label_14->setText(QApplication::translate("MainWindow", "CCW ANGLE LIMIT", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("MainWindow", "Model", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("MainWindow", "D Gain", 0, QApplication::UnicodeUTF8));
        label_8->setText(QApplication::translate("MainWindow", "I Gain", 0, QApplication::UnicodeUTF8));
        label_9->setText(QApplication::translate("MainWindow", "P Gain", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // PROGRAMLX3073_H
