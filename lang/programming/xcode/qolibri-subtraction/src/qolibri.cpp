/***************************************************************************
*   Copyright (C) 2007 by BOP                                             *
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
*   This program is distributed in the hope that it will be useful,       *
*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
*   GNU General Public License for more details.                          *
*                                                                         *
*   You should have received a copy of the GNU General Public License     *
*   along with this program; if not, write to the                         *
*   Free Software Foundation, Inc.,                                       *
*   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
***************************************************************************/

#include "ebook.h"
#include "book.h"

#include "ebcache.h"
#include "mainwindow.h"
#include "configure.h"
#include "method.h"
#include "model.h"
#include "server.h"
#include "client.h"

#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <QApplication>
#include <QLibraryInfo>
#include <QLocale>
#include <QTranslator>
#ifdef USE_STATIC_PLUGIN
#include <QtPlugin>
#endif

#if defined (USE_STATIC_PLUGIN)
Q_IMPORT_PLUGIN(qjpcodecs)
Q_IMPORT_PLUGIN(qjpeg)
#endif

const char * const usage =
    "\n"
    "Usage:\n"
    "   qolibri [argument] [search text...] \n"
    "\n"
    "Arguments:\n"
    "   -s                Client/Server mode\n"
    "   -p <port-no>      Server Port no (default:5626)\n"
    "   -c <session name> Configuration session name\n"
    "   -h  or  --help    Print Help (this message) and exit\n"
    "   --version         Print version information and exit";

const char *version =
    "qolibri - EPWING Dictionary/Book Viewer " QOLIBRI_VERSION_STR;

QoServer *server;

extern Configure *configure_s;

EB_Error_Code myHookBEGIN_IN_COLOR_JPEG(EB_Book *book, EB_Appendix*a,
    void *classp, EB_Hook_Code c, int argc, const unsigned int* argv)
{
    EB_Position pos;
    pos.page = argv[2];
    pos.offset = argv[3];

    return EB_SUCCESS;
}

EB_Hook myhooks[] = {
  { EB_HOOK_BEGIN_IN_COLOR_JPEG, myHookBEGIN_IN_COLOR_JPEG },
  { EB_HOOK_NULL, NULL }
};

void starthook() {

    const char * errs;
    const char * errmsg;

    EB_Book book;
    EB_Appendix appendix;
    EB_Hookset hookset;

    eb_initialize_library();
    eb_initialize_book(&book);
    eb_initialize_appendix(&appendix);
    eb_initialize_hookset(&hookset);

    EB_Error_Code ecode;

    ecode = eb_set_hooks(&hookset, myhooks);
    ecode = eb_bind( &book,"/Users/vvw/Documents/dic/NHK");  // path.toUtf8();

    EB_Subbook_Code codes[EB_MAX_SUBBOOKS];
    int cnt;

    ecode = eb_subbook_list(&book, codes, &cnt);
    ecode = eb_set_subbook(&book, codes[0]);
    if( ecode != EB_SUCCESS )
    {
      errs =  eb_error_string( ecode );
      errmsg = eb_error_message( ecode );

    }

    EB_Position pos;
    ecode = eb_text(&book, &pos);  // first word position

    ecode = eb_seek_text(&book, &pos);

    char buff[1024+1];
    ssize_t len;

    ecode = eb_read_text(&book, &appendix, &hookset, NULL,  // 可以传void** 进去，发生回调的时侯别人会原样回传给你
                1024, buff, &len);
}

int main(int argc, char *argv[])
{
    Q_INIT_RESOURCE(qolibri);

    QGuiApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
    QApplication app(argc, argv);

    configure_s = new Configure();
    CONF->load();
    EbCache::initialize();

    Model model;
    model.load();

    QString searchText;
    qint16 port = CONF->portNo;
    bool qserv = CONF->serverMode;

    for(int i=1; i<argc; i++){
        QString str = QString::fromLocal8Bit(argv[i]);
        if (str == "-c" && (i+1) < argc) {
            CONF->settingOrg = QString::fromLocal8Bit(argv[i+1]);
            i++;

        } else if (str == "-p" && (i+1) < argc) {
            bool ok;
            port = QString::fromLocal8Bit(argv[i+1]).toInt(&ok);
            if (ok) {
                i++;
            } else {
                qWarning() << "can't convert port no (" << argv[i+1] << ")";
            }
        } else if (str == "-s") {
            qserv = true;
        } else if (str == "-h" || str == "--help") {
            qDebug() << version;
            qDebug() << usage;
            return 1;
        } else if (str == "--version") {
            qDebug() << version;
            return 1;
        } else {
            searchText += str;
            if ( (i+1) < argc) searchText += " ";
        }
    }

    if (qserv) {
        QoClient client("localhost", port);
        if (client.connectHost()) {
            client.sendText(searchText.toLocal8Bit());
            //client.disconnectFromHost();
            return 1;
        }
    }

    QTranslator qtTranslator;
    if (qtTranslator.load("qt_" + QLocale::system().name(), QLibraryInfo::location(QLibraryInfo::TranslationsPath)))
        QApplication::installTranslator(&qtTranslator);

    QTranslator trans;
    QString thename(QStringLiteral(":/translations/qolibri_") + QLocale::system().name());
    if (trans.load(thename))
        QApplication::installTranslator(&trans);


    //QEb::initialize();
    //eb_initialize_library();
    //extern void starthook();
    starthook();

    MainWindow mainWin(&model, searchText);


    mainWin.show();

    if (qserv) {
        server = new QoServer(port);
        server->slotSearchText(&mainWin,
                               SLOT(searchClientText(const QString&)));
        server->slotShowStatus(&mainWin,
                               SLOT(showStatus(const QString&)));
        server->showStatus(QString("Start as server (port = %1)")
                                  .arg(server->serverPort()));
    }
    //if (!searchText.isEmpty()) {
    //    emit mainWin.searchClientText(searchText);
    //}


    int ret = app.exec();

    delete server;
    model.save();

    return ret;
}

