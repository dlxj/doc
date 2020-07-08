/****************************************************************************
** Meta object code from reading C++ file 'helpwindow.hh'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../goldendict/helpwindow.hh"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'helpwindow.hh' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Help__HelpBrowser[] = {

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
      23,   19,   18,   18, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_Help__HelpBrowser[] = {
    "Help::HelpBrowser\0\0url\0linkClicked(QUrl)\0"
};

void Help::HelpBrowser::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        HelpBrowser *_t = static_cast<HelpBrowser *>(_o);
        switch (_id) {
        case 0: _t->linkClicked((*reinterpret_cast< const QUrl(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Help::HelpBrowser::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Help::HelpBrowser::staticMetaObject = {
    { &QTextBrowser::staticMetaObject, qt_meta_stringdata_Help__HelpBrowser,
      qt_meta_data_Help__HelpBrowser, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Help::HelpBrowser::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Help::HelpBrowser::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Help::HelpBrowser::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Help__HelpBrowser))
        return static_cast<void*>(const_cast< HelpBrowser*>(this));
    return QTextBrowser::qt_metacast(_clname);
}

int Help::HelpBrowser::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QTextBrowser::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}
static const uint qt_meta_data_Help__HelpWindow[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       9,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      18,   17,   17,   17, 0x05,

 // slots: signature, parameters, type, tag, flags
      30,   17,   17,   17, 0x0a,
      39,   17,   17,   17, 0x0a,
      56,   48,   17,   17, 0x0a,
      77,   48,   17,   17, 0x0a,
     105,   99,   17,   17, 0x0a,
     138,   17,   17,   17, 0x0a,
     147,   17,   17,   17, 0x0a,
     157,   17,   17,   17, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_Help__HelpWindow[] = {
    "Help::HelpWindow\0\0needClose()\0reject()\0"
    "accept()\0enabled\0forwardEnabled(bool)\0"
    "backwardEnabled(bool)\0index\0"
    "contentsItemClicked(QModelIndex)\0"
    "zoomIn()\0zoomOut()\0zoomBase()\0"
};

void Help::HelpWindow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        HelpWindow *_t = static_cast<HelpWindow *>(_o);
        switch (_id) {
        case 0: _t->needClose(); break;
        case 1: _t->reject(); break;
        case 2: _t->accept(); break;
        case 3: _t->forwardEnabled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->backwardEnabled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: _t->contentsItemClicked((*reinterpret_cast< const QModelIndex(*)>(_a[1]))); break;
        case 6: _t->zoomIn(); break;
        case 7: _t->zoomOut(); break;
        case 8: _t->zoomBase(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Help::HelpWindow::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Help::HelpWindow::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_Help__HelpWindow,
      qt_meta_data_Help__HelpWindow, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Help::HelpWindow::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Help::HelpWindow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Help::HelpWindow::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Help__HelpWindow))
        return static_cast<void*>(const_cast< HelpWindow*>(this));
    return QDialog::qt_metacast(_clname);
}

int Help::HelpWindow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 9)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
    }
    return _id;
}

// SIGNAL 0
void Help::HelpWindow::needClose()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}
QT_END_MOC_NAMESPACE
