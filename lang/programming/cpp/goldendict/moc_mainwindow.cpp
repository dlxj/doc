/****************************************************************************
** Meta object code from reading C++ file 'mainwindow.hh'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../goldendict/mainwindow.hh"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'mainwindow.hh' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_ExpandableToolBar[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       0,    0, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

       0        // eod
};

static const char qt_meta_stringdata_ExpandableToolBar[] = {
    "ExpandableToolBar\0"
};

void ExpandableToolBar::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData ExpandableToolBar::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject ExpandableToolBar::staticMetaObject = {
    { &QToolBar::staticMetaObject, qt_meta_stringdata_ExpandableToolBar,
      qt_meta_data_ExpandableToolBar, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &ExpandableToolBar::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *ExpandableToolBar::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *ExpandableToolBar::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_ExpandableToolBar))
        return static_cast<void*>(const_cast< ExpandableToolBar*>(this));
    return QToolBar::qt_metacast(_clname);
}

int ExpandableToolBar::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QToolBar::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    return _id;
}
static const uint qt_meta_data_MainWindow[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
     132,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       3,       // signalCount

 // signals: signature, parameters, type, tag, flags
      19,   12,   11,   11, 0x05,
      51,   48,   11,   11, 0x05,
      81,   76,   11,   11, 0x05,

 // slots: signature, parameters, type, tag, flags
     110,   11,   11,   11, 0x0a,
     157,  154,   11,   11, 0x0a,
     199,   11,   11,   11, 0x0a,
     223,  221,   11,   11, 0x0a,
     257,   12,   11,   11, 0x0a,
     277,  221,   11,   11, 0x0a,
     316,   11,   11,   11, 0x0a,
     326,   11,   11,   11, 0x08,
     347,   11,   11,   11, 0x08,
     373,   11,   11,   11, 0x08,
     394,   11,   11,   11, 0x08,
     425,  420,   11,   11, 0x08,
     469,  465,   11,   11, 0x08,
     508,   48,   11,   11, 0x08,
     536,   48,   11,   11, 0x08,
     569,   48,   11,   11, 0x08,
     604,  599,   11,   11, 0x08,
     639,   76,   11,   11, 0x08,
     668,   11,   11,   11, 0x08,
     697,   11,   11,   11, 0x08,
     724,   11,   11,   11, 0x08,
     748,   11,   11,   11, 0x08,
     760,   11,   11,   11, 0x08,
     783,   11,   11,   11, 0x08,
     801,   11,   11,   11, 0x08,
     816,   11,   11,   11, 0x08,
     832,   11,   11,   11, 0x08,
     850,   11,   11,   11, 0x08,
     868,   11,   11,   11, 0x08,
     883,   11,   11,   11, 0x08,
     915,   11,   11,   11, 0x08,
     931,   11,   11,   11, 0x08,
     953,  949,   11,   11, 0x08,
     978,   11,   11,   11, 0x08,
     992,   11,   11,   11, 0x08,
    1009,  221,   11,   11, 0x08,
    1044,  221,   11,   11, 0x08,
    1076,   11,   11,   11, 0x08,
    1101,   11,   11,   11, 0x08,
    1118,  465,   11,   11, 0x08,
    1151, 1143,   11,   11, 0x08,
    1183, 1178,   11,   11, 0x08,
    1207,   11,   11,   11, 0x28,
    1219,   11,   11,   11, 0x08,
    1228,   11,   11,   11, 0x08,
    1238,   11,   11,   11, 0x08,
    1247,   11,   11,   11, 0x08,
    1282,   11,   11,   11, 0x08,
    1298,   11,   11,   11, 0x08,
    1315,   11,   11,   11, 0x08,
    1333,   11,   11,   11, 0x08,
    1375, 1355,   11,   11, 0x08,
    1398,   11,   11,   11, 0x28,
    1417,   11,   11,   11, 0x08,
    1436,   11,   11,   11, 0x08,
    1454,   11,   11,   11, 0x08,
    1483,   11,   11,   11, 0x08,
    1536, 1514,   11,   11, 0x08,
    1588, 1573,   11,   11, 0x28,
    1617,   11,   11,   11, 0x28,
    1642,   11,   11,   11, 0x08,
    1654,   11,   11,   11, 0x08,
    1675,   11,   11,   11, 0x08,
    1715,   11,   11,   11, 0x08,
    1742,   11,   11,   11, 0x08,
    1783,   11,   11,   11, 0x08,
    1818, 1811,   11,   11, 0x08,
    1858,   11,   11,   11, 0x28,
    1893,   11,   11,   11, 0x08,
    1909,   11,   11,   11, 0x08,
    1971, 1955, 1942,   11, 0x08,
    2010, 1998,   11,   11, 0x08,
    2100, 2068,   11,   11, 0x08,
    2167,   11,   11,   11, 0x08,
    2192, 2188,   11,   11, 0x08,
    2241,   11,   11,   11, 0x08,
    2284, 2268,   11,   11, 0x08,
    2334, 2325,   11,   11, 0x28,
    2367,   11,   11,   11, 0x28,
    2434, 2395,   11,   11, 0x08,
    2487,   11,   11,   11, 0x08,
    2512,   11,   11,   11, 0x08,
    2565,   11,   11,   11, 0x08,
    2589,   11,   11,   11, 0x08,
    2608,   11,   11,   11, 0x08,
    2625,   11,   11,   11, 0x08,
    2641,   11,   11,   11, 0x08,
    2654,   11,   11,   11, 0x08,
    2673,   11,   11,   11, 0x08,
    2685,   11,   11,   11, 0x08,
    2713,   11,   11,   11, 0x08,
    2757, 2748,   11,   11, 0x08,
    2786,   11,   11,   11, 0x28,
    2811,   11,   11,   11, 0x08,
    2839,   11,   11,   11, 0x08,
    2861,   11,   11,   11, 0x08,
    2894,   11,   11,   11, 0x08,
    2919,   11,   11,   11, 0x08,
    2947,   11,   11,   11, 0x08,
    2968,   11,   11,   11, 0x08,
    3006,   11,   11,   11, 0x08,
    3033,   11,   11,   11, 0x08,
    3060,   11,   11,   11, 0x08,
    3093,   11,   11,   11, 0x08,
    3124,   11,   11,   11, 0x08,
    3153,   11,   11,   11, 0x08,
    3182, 1143,   11,   11, 0x08,
    3213,   11,   11,   11, 0x08,
    3229,   11,   11,   11, 0x08,
    3260,   11,   11,   11, 0x08,
    3291,   11,   11,   11, 0x08,
    3341, 3328,   11,   11, 0x08,
    3370,   11,   11,   11, 0x08,
    3392,   11,   11,   11, 0x08,
    3417, 3412,   11,   11, 0x08,
    3443, 3412,   11,   11, 0x08,
    3487, 3474,   11,   11, 0x08,
    3525, 3474, 3520,   11, 0x08,
    3566, 3412,   11,   11, 0x08,
    3595,   11,   11,   11, 0x08,
    3626,   11,   11,   11, 0x08,
    3649,   11,   11,   11, 0x08,
    3672,   11,   11,   11, 0x08,
    3711, 3691,   11,   11, 0x08,
    3762,   11,   11,   11, 0x08,
    3789,   11,   11,   11, 0x08,
    3817,   11,   11,   11, 0x08,
    3830,   11,   11,   11, 0x08,
    3848, 3843, 3520,   11, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_MainWindow[] = {
    "MainWindow\0\0expand\0setExpandOptionalParts(bool)\0"
    "id\0clickOnDictPane(QString)\0name\0"
    "setPopupGroupByName(QString)\0"
    "messageFromAnotherInstanceReceived(QString)\0"
    ",,\0showStatusBarMessage(QString,int,QPixmap)\0"
    "wordReceived(QString)\0,\0"
    "headwordReceived(QString,QString)\0"
    "setExpandMode(bool)\0"
    "headwordFromFavorites(QString,QString)\0"
    "quitApp()\0hotKeyActivated(int)\0"
    "prepareNewReleaseChecks()\0"
    "checkForNewRelease()\0latestReleaseReplyReady()\0"
    "item\0foundDictsPaneClicked(QListWidgetItem*)\0"
    "pos\0foundDictsContextMenuRequested(QPoint)\0"
    "showDictionaryInfo(QString)\0"
    "showDictionaryHeadwords(QString)\0"
    "openDictionaryFolder(QString)\0dict\0"
    "editDictionary(Dictionary::Class*)\0"
    "showFTSIndexingName(QString)\0"
    "handleAddToFavoritesButton()\0"
    "addCurrentTabToFavorites()\0"
    "addAllTabsToFavorites()\0addNewTab()\0"
    "tabCloseRequested(int)\0closeCurrentTab()\0"
    "closeAllTabs()\0closeRestTabs()\0"
    "switchToNextTab()\0switchToPrevTab()\0"
    "ctrlReleased()\0switchExpandOptionalPartsMode()\0"
    "createTabList()\0fillWindowsMenu()\0act\0"
    "switchToWindow(QAction*)\0backClicked()\0"
    "forwardClicked()\0titleChanged(ArticleView*,QString)\0"
    "iconChanged(ArticleView*,QIcon)\0"
    "pageLoaded(ArticleView*)\0tabSwitched(int)\0"
    "tabMenuRequested(QPoint)\0checked\0"
    "dictionaryBarToggled(bool)\0view\0"
    "pronounce(ArticleView*)\0pronounce()\0"
    "zoomin()\0zoomout()\0unzoom()\0"
    "scaleArticlesByCurrentZoomFactor()\0"
    "doWordsZoomIn()\0doWordsZoomOut()\0"
    "doWordsZoomBase()\0applyWordsZoomLevel()\0"
    "editDictionaryGroup\0editDictionaries(uint)\0"
    "editDictionaries()\0editCurrentGroup()\0"
    "editPreferences()\0currentGroupChanged(QString)\0"
    "translateInputChanged(QString)\0"
    "checkModifiers,dictID\0"
    "translateInputFinished(bool,QString)\0"
    "checkModifiers\0translateInputFinished(bool)\0"
    "translateInputFinished()\0handleEsc()\0"
    "focusTranslateLine()\0"
    "wordListItemActivated(QListWidgetItem*)\0"
    "wordListSelectionChanged()\0"
    "dictsListItemActivated(QListWidgetItem*)\0"
    "dictsListSelectionChanged()\0,force\0"
    "jumpToDictionary(QListWidgetItem*,bool)\0"
    "jumpToDictionary(QListWidgetItem*)\0"
    "showDictsPane()\0dictsPaneVisibilityChanged(bool)\0"
    "ArticleView*\0switchToIt,name\0"
    "createNewTab(bool,QString)\0,,,contexts\0"
    "openLinkInNewTab(QUrl,QUrl,QString,ArticleView::Contexts)\0"
    "word,group,fromArticle,contexts\0"
    "showDefinitionInNewTab(QString,uint,QString,ArticleView::Contexts)\0"
    "typingEvent(QString)\0,id\0"
    "activeArticleChanged(const ArticleView*,QString)\0"
    "mutedDictionariesChanged()\0,inGroup,dictID\0"
    "showTranslationFor(QString,uint,QString)\0"
    ",inGroup\0showTranslationFor(QString,uint)\0"
    "showTranslationFor(QString)\0"
    ",dictIDs,searchRegExp,ignoreDiacritics\0"
    "showTranslationFor(QString,QStringList,QRegExp,bool)\0"
    "showHistoryItem(QString)\0"
    "trayIconActivated(QSystemTrayIcon::ActivationReason)\0"
    "scanEnableToggled(bool)\0setAutostart(bool)\0"
    "showMainWindow()\0visitHomepage()\0"
    "visitForum()\0openConfigFolder()\0"
    "showAbout()\0showDictBarNamesTriggered()\0"
    "useSmallIconsInToolbarsTriggered()\0"
    "announce\0toggleMenuBarTriggered(bool)\0"
    "toggleMenuBarTriggered()\0"
    "on_clearHistory_triggered()\0"
    "on_newTab_triggered()\0"
    "on_actionCloseToTray_triggered()\0"
    "on_pageSetup_triggered()\0"
    "on_printPreview_triggered()\0"
    "on_print_triggered()\0"
    "printPreviewPaintRequested(QPrinter*)\0"
    "on_saveArticle_triggered()\0"
    "on_rescanFiles_triggered()\0"
    "on_showHideFavorites_triggered()\0"
    "on_showHideHistory_triggered()\0"
    "on_exportHistory_triggered()\0"
    "on_importHistory_triggered()\0"
    "on_alwaysOnTop_triggered(bool)\0"
    "focusWordList()\0on_exportFavorites_triggered()\0"
    "on_importFavorites_triggered()\0"
    "on_ExportFavoritesToList_triggered()\0"
    "searchInDock\0updateSearchPaneAndBar(bool)\0"
    "updateFavoritesMenu()\0updateHistoryMenu()\0"
    "word\0addWordToHistory(QString)\0"
    "forceAddWordToHistory(QString)\0"
    "word,groupId\0addWordToFavorites(QString,uint)\0"
    "bool\0isWordPresentedInFavorites(QString,uint)\0"
    "sendWordToInputLine(QString)\0"
    "storeResourceSavePath(QString)\0"
    "closeHeadwordsDialog()\0focusHeadwordsDialog()\0"
    "focusArticleView()\0proxy,authenticator\0"
    "proxyAuthentication(QNetworkProxy,QAuthenticator*)\0"
    "showFullTextSearchDialog()\0"
    "closeFullTextSearchDialog()\0showGDHelp()\0"
    "hideGDHelp()\0hwnd\0isGoldenDictWindow(HWND)\0"
};

void MainWindow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        MainWindow *_t = static_cast<MainWindow *>(_o);
        switch (_id) {
        case 0: _t->setExpandOptionalParts((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->clickOnDictPane((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 2: _t->setPopupGroupByName((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 3: _t->messageFromAnotherInstanceReceived((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 4: _t->showStatusBarMessage((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2])),(*reinterpret_cast< const QPixmap(*)>(_a[3]))); break;
        case 5: _t->wordReceived((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 6: _t->headwordReceived((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 7: _t->setExpandMode((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 8: _t->headwordFromFavorites((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 9: _t->quitApp(); break;
        case 10: _t->hotKeyActivated((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 11: _t->prepareNewReleaseChecks(); break;
        case 12: _t->checkForNewRelease(); break;
        case 13: _t->latestReleaseReplyReady(); break;
        case 14: _t->foundDictsPaneClicked((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 15: _t->foundDictsContextMenuRequested((*reinterpret_cast< const QPoint(*)>(_a[1]))); break;
        case 16: _t->showDictionaryInfo((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 17: _t->showDictionaryHeadwords((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 18: _t->openDictionaryFolder((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 19: _t->editDictionary((*reinterpret_cast< Dictionary::Class*(*)>(_a[1]))); break;
        case 20: _t->showFTSIndexingName((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 21: _t->handleAddToFavoritesButton(); break;
        case 22: _t->addCurrentTabToFavorites(); break;
        case 23: _t->addAllTabsToFavorites(); break;
        case 24: _t->addNewTab(); break;
        case 25: _t->tabCloseRequested((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 26: _t->closeCurrentTab(); break;
        case 27: _t->closeAllTabs(); break;
        case 28: _t->closeRestTabs(); break;
        case 29: _t->switchToNextTab(); break;
        case 30: _t->switchToPrevTab(); break;
        case 31: _t->ctrlReleased(); break;
        case 32: _t->switchExpandOptionalPartsMode(); break;
        case 33: _t->createTabList(); break;
        case 34: _t->fillWindowsMenu(); break;
        case 35: _t->switchToWindow((*reinterpret_cast< QAction*(*)>(_a[1]))); break;
        case 36: _t->backClicked(); break;
        case 37: _t->forwardClicked(); break;
        case 38: _t->titleChanged((*reinterpret_cast< ArticleView*(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 39: _t->iconChanged((*reinterpret_cast< ArticleView*(*)>(_a[1])),(*reinterpret_cast< const QIcon(*)>(_a[2]))); break;
        case 40: _t->pageLoaded((*reinterpret_cast< ArticleView*(*)>(_a[1]))); break;
        case 41: _t->tabSwitched((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 42: _t->tabMenuRequested((*reinterpret_cast< QPoint(*)>(_a[1]))); break;
        case 43: _t->dictionaryBarToggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 44: _t->pronounce((*reinterpret_cast< ArticleView*(*)>(_a[1]))); break;
        case 45: _t->pronounce(); break;
        case 46: _t->zoomin(); break;
        case 47: _t->zoomout(); break;
        case 48: _t->unzoom(); break;
        case 49: _t->scaleArticlesByCurrentZoomFactor(); break;
        case 50: _t->doWordsZoomIn(); break;
        case 51: _t->doWordsZoomOut(); break;
        case 52: _t->doWordsZoomBase(); break;
        case 53: _t->applyWordsZoomLevel(); break;
        case 54: _t->editDictionaries((*reinterpret_cast< uint(*)>(_a[1]))); break;
        case 55: _t->editDictionaries(); break;
        case 56: _t->editCurrentGroup(); break;
        case 57: _t->editPreferences(); break;
        case 58: _t->currentGroupChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 59: _t->translateInputChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 60: _t->translateInputFinished((*reinterpret_cast< bool(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 61: _t->translateInputFinished((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 62: _t->translateInputFinished(); break;
        case 63: _t->handleEsc(); break;
        case 64: _t->focusTranslateLine(); break;
        case 65: _t->wordListItemActivated((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 66: _t->wordListSelectionChanged(); break;
        case 67: _t->dictsListItemActivated((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 68: _t->dictsListSelectionChanged(); break;
        case 69: _t->jumpToDictionary((*reinterpret_cast< QListWidgetItem*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 70: _t->jumpToDictionary((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 71: _t->showDictsPane(); break;
        case 72: _t->dictsPaneVisibilityChanged((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 73: { ArticleView* _r = _t->createNewTab((*reinterpret_cast< bool(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2])));
            if (_a[0]) *reinterpret_cast< ArticleView**>(_a[0]) = _r; }  break;
        case 74: _t->openLinkInNewTab((*reinterpret_cast< const QUrl(*)>(_a[1])),(*reinterpret_cast< const QUrl(*)>(_a[2])),(*reinterpret_cast< const QString(*)>(_a[3])),(*reinterpret_cast< const ArticleView::Contexts(*)>(_a[4]))); break;
        case 75: _t->showDefinitionInNewTab((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< uint(*)>(_a[2])),(*reinterpret_cast< const QString(*)>(_a[3])),(*reinterpret_cast< const ArticleView::Contexts(*)>(_a[4]))); break;
        case 76: _t->typingEvent((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 77: _t->activeArticleChanged((*reinterpret_cast< const ArticleView*(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 78: _t->mutedDictionariesChanged(); break;
        case 79: _t->showTranslationFor((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< uint(*)>(_a[2])),(*reinterpret_cast< const QString(*)>(_a[3]))); break;
        case 80: _t->showTranslationFor((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< uint(*)>(_a[2]))); break;
        case 81: _t->showTranslationFor((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 82: _t->showTranslationFor((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const QStringList(*)>(_a[2])),(*reinterpret_cast< const QRegExp(*)>(_a[3])),(*reinterpret_cast< bool(*)>(_a[4]))); break;
        case 83: _t->showHistoryItem((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 84: _t->trayIconActivated((*reinterpret_cast< QSystemTrayIcon::ActivationReason(*)>(_a[1]))); break;
        case 85: _t->scanEnableToggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 86: _t->setAutostart((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 87: _t->showMainWindow(); break;
        case 88: _t->visitHomepage(); break;
        case 89: _t->visitForum(); break;
        case 90: _t->openConfigFolder(); break;
        case 91: _t->showAbout(); break;
        case 92: _t->showDictBarNamesTriggered(); break;
        case 93: _t->useSmallIconsInToolbarsTriggered(); break;
        case 94: _t->toggleMenuBarTriggered((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 95: _t->toggleMenuBarTriggered(); break;
        case 96: _t->on_clearHistory_triggered(); break;
        case 97: _t->on_newTab_triggered(); break;
        case 98: _t->on_actionCloseToTray_triggered(); break;
        case 99: _t->on_pageSetup_triggered(); break;
        case 100: _t->on_printPreview_triggered(); break;
        case 101: _t->on_print_triggered(); break;
        case 102: _t->printPreviewPaintRequested((*reinterpret_cast< QPrinter*(*)>(_a[1]))); break;
        case 103: _t->on_saveArticle_triggered(); break;
        case 104: _t->on_rescanFiles_triggered(); break;
        case 105: _t->on_showHideFavorites_triggered(); break;
        case 106: _t->on_showHideHistory_triggered(); break;
        case 107: _t->on_exportHistory_triggered(); break;
        case 108: _t->on_importHistory_triggered(); break;
        case 109: _t->on_alwaysOnTop_triggered((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 110: _t->focusWordList(); break;
        case 111: _t->on_exportFavorites_triggered(); break;
        case 112: _t->on_importFavorites_triggered(); break;
        case 113: _t->on_ExportFavoritesToList_triggered(); break;
        case 114: _t->updateSearchPaneAndBar((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 115: _t->updateFavoritesMenu(); break;
        case 116: _t->updateHistoryMenu(); break;
        case 117: _t->addWordToHistory((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 118: _t->forceAddWordToHistory((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 119: _t->addWordToFavorites((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< uint(*)>(_a[2]))); break;
        case 120: { bool _r = _t->isWordPresentedInFavorites((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< uint(*)>(_a[2])));
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = _r; }  break;
        case 121: _t->sendWordToInputLine((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 122: _t->storeResourceSavePath((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 123: _t->closeHeadwordsDialog(); break;
        case 124: _t->focusHeadwordsDialog(); break;
        case 125: _t->focusArticleView(); break;
        case 126: _t->proxyAuthentication((*reinterpret_cast< const QNetworkProxy(*)>(_a[1])),(*reinterpret_cast< QAuthenticator*(*)>(_a[2]))); break;
        case 127: _t->showFullTextSearchDialog(); break;
        case 128: _t->closeFullTextSearchDialog(); break;
        case 129: _t->showGDHelp(); break;
        case 130: _t->hideGDHelp(); break;
        case 131: { bool _r = _t->isGoldenDictWindow((*reinterpret_cast< HWND(*)>(_a[1])));
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = _r; }  break;
        default: ;
        }
    }
}

const QMetaObjectExtraData MainWindow::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject MainWindow::staticMetaObject = {
    { &QMainWindow::staticMetaObject, qt_meta_stringdata_MainWindow,
      qt_meta_data_MainWindow, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &MainWindow::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *MainWindow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *MainWindow::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_MainWindow))
        return static_cast<void*>(const_cast< MainWindow*>(this));
    if (!strcmp(_clname, "DataCommitter"))
        return static_cast< DataCommitter*>(const_cast< MainWindow*>(this));
    return QMainWindow::qt_metacast(_clname);
}

int MainWindow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 132)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 132;
    }
    return _id;
}

// SIGNAL 0
void MainWindow::setExpandOptionalParts(bool _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void MainWindow::clickOnDictPane(QString const & _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void MainWindow::setPopupGroupByName(QString const & _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}
static const uint qt_meta_data_ArticleSaveProgressDialog[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       1,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      27,   26,   26,   26, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_ArticleSaveProgressDialog[] = {
    "ArticleSaveProgressDialog\0\0perform()\0"
};

void ArticleSaveProgressDialog::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        ArticleSaveProgressDialog *_t = static_cast<ArticleSaveProgressDialog *>(_o);
        switch (_id) {
        case 0: _t->perform(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData ArticleSaveProgressDialog::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject ArticleSaveProgressDialog::staticMetaObject = {
    { &QProgressDialog::staticMetaObject, qt_meta_stringdata_ArticleSaveProgressDialog,
      qt_meta_data_ArticleSaveProgressDialog, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &ArticleSaveProgressDialog::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *ArticleSaveProgressDialog::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *ArticleSaveProgressDialog::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_ArticleSaveProgressDialog))
        return static_cast<void*>(const_cast< ArticleSaveProgressDialog*>(this));
    return QProgressDialog::qt_metacast(_clname);
}

int ArticleSaveProgressDialog::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QProgressDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
