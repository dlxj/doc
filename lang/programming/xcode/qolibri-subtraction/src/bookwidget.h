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
#ifndef BOOKWIDGET_H
#define BOOKWIDGET_H

#include "book.h"

#include <QPushButton>
#include <QLabel>

class QPushButton;

class Book;
class Group;

class BookWidget : public QWidget
{
    Q_OBJECT
public:
    BookWidget(Group *grp, QWidget *parent);
    void initBook(Group *grp);
    bool addBook(const QString &name, BookType btype,
                 const QString &path, int subbook );
    inline QListWidget *bookListWidget() const
    {
        return bookListWidget_;
    }
    inline int currentRow() const
    {
        return bookListWidget_->currentRow();
    }
    inline Book *currentBook() const
    {
        return group->bookList().at(currentRow());
    }
    QList <QListWidgetItem*> selectedBooks() const
    {
        return bookListWidget_->selectedItems();
    }
    inline QListWidgetItem *currentItem() const
    {
        return bookListWidget_->currentItem();
    }
    inline void setCurrentRow(int row) const
    {
        bookListWidget_->setCurrentRow(row);
    }
    void hideDelButton() { delButton->hide(); }
    void hideViewButton() { viewButton->hide(); }
    void hideFontButton() { fontButton->hide(); }
    void hideEditButton() { editButton_->hide(); }
    void hideAddButton() { addButton_->hide(); }
    void hideGroupName() { groupNameLabel->hide(); }
    QPushButton *addButton() { return addButton_; }
    QPushButton *editButton() { return editButton_; }

signals:
    void rowChanged(int row);
    void bookViewRequested(Book *book);
    void fontViewRequested(Book *book);

private slots:
    void upItem();
    void downItem();
    void delItem();
    void viewItem()
    {
        emit bookViewRequested(group->bookList().at(currentRow()));
    }
    void editItem(QListWidgetItem* item)
    {
        if (editButton_->isVisible()) {
            bookListWidget_->openPersistentEditor(item);
            bookListWidget_->editItem(item);
        }
    }
    void editItem()
    {
        editItem(currentItem());
    }

    void setFont()
    {
        emit fontViewRequested(currentBook());
    }

    void changeRow()
    {
        resetButtons();
    }
    void changeName(QListWidgetItem *item)
    {
        ((Book *)item)->setName(item->text());
    }
    void changeSelect(QListWidgetItem*, QListWidgetItem* prev)
    {
        bookListWidget_->closePersistentEditor(prev);
    }


private:
    void resetButtons();

    QListWidget *bookListWidget_;
    QLabel *groupNameLabel;
    QPushButton *upButton;
    QPushButton *downButton;
    QPushButton *delButton;
    QPushButton *viewButton;
    QPushButton *fontButton;
    QPushButton *editButton_;
    QPushButton *addButton_;

    Group *group;
};


#endif
