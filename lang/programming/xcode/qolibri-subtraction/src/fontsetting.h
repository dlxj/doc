/***************************************************************************
*   Copyright (C) 2007 by BOP                                             *
*   polepolek@gmail.com                                                   *
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
#ifndef FONTSETTING_H
#define FONTSETTING_H

#include "book.h"

#include <QDialog>

class QTreeWidget;
class QTreeWidgetItem;
class QLabel;

class FontSetting : public QDialog
{
    Q_OBJECT
public:
    FontSetting(Book *book, QWidget *parent);
    int setupTreeWidget(const QString &fpath);
    QHash <QString, QString>  *newAlternateFontList();

private slots:
    void selectFont(QTreeWidgetItem *next, QTreeWidgetItem *prev);
    void changeFontCode(const QString &txt);
    void save();
    void load();

private:

    QPushButton *fontButton;
    QLabel *fontCodeLabel;
    QTreeWidget *fontTreeWidget;
    QLineEdit *fontCodeEdit;
    QLabel *fontLabel;
    QString cacheDir;
    Book *book;
};

#endif
