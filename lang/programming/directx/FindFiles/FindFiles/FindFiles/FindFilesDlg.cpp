// FindFilesDlg.cpp : implementation file
//

#include "stdafx.h"
#include "FindFiles.h"
#include "FindFilesDlg.h"
#include "FileFinder.h"
#include "Path.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CFindFilesDlg dialog

CFindFilesDlg::CFindFilesDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CFindFilesDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CFindFilesDlg)
	m_bSize = FALSE;
	m_bSubFolders = TRUE;
	m_sFileMask = _T("");
	m_nMaxSize = 0;
	m_nMinSize = 0;
	m_sBaseFolder = _T("");
	m_sFindText = _T("");
	m_nSearchType = 0;
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
	_bSearching = false;
}

void CFindFilesDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CFindFilesDlg)
	DDX_Control(pDX, IDC_LIST, m_list);
	DDX_Check(pDX, IDC_CKSIZE, m_bSize);
	DDX_Check(pDX, IDC_CKSUBFOLDERS, m_bSubFolders);
	DDX_Text(pDX, IDC_EDITMASK, m_sFileMask);
	DDX_Text(pDX, IDC_EDITMAXSIZE, m_nMaxSize);
	DDX_Text(pDX, IDC_EDITMINSIZE, m_nMinSize);
	DDX_Text(pDX, IDC_EDITROOT, m_sBaseFolder);
	DDX_Text(pDX, IDC_EDITTEXT, m_sFindText);
	DDX_Radio(pDX, IDC_RDSEARCHREPLACE, m_nSearchType);
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CFindFilesDlg, CDialog)
	//{{AFX_MSG_MAP(CFindFilesDlg)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_WM_CREATE()
	ON_WM_GETMINMAXINFO()
	ON_WM_SIZE()
	ON_BN_CLICKED(IDC_CKSIZE, OnCheckSize)
	ON_BN_CLICKED(IDOK, OnSearch)
	ON_BN_CLICKED(IDC_BTBROWSE, OnBrowse)
	ON_NOTIFY(NM_DBLCLK, IDC_LIST, OnDblclkList)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CFindFilesDlg message handlers

BOOL CFindFilesDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Set the icon for this dialog.
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	// Image list
	_imgList.Create(16, 16, ILC_COLOR24 | ILC_MASK, 1, 1);
	_imgList.Add(AfxGetApp()->LoadIcon(IDI_MATCH));
	
	// List initialization
	m_list.InsertColumn(0, "Name", LVCFMT_LEFT, 150, 0);
	m_list.InsertColumn(1, "In Folder", LVCFMT_LEFT, 200, 1);
	m_list.InsertColumn(2, "Size", LVCFMT_LEFT, 60, 2);
	m_list.InsertColumn(3, "Modified", LVCFMT_LEFT, 120, 3);

	m_list.SetImageList(&_imgList, LVSIL_SMALL);

	// Set callback function
	_finder.SetCallback(FileFinderProc, this);

	
	return TRUE;
}

void CFindFilesDlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this to obtain the cursor to display
// while the user drags the minimized window.
HCURSOR CFindFilesDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

int CFindFilesDlg::OnCreate(LPCREATESTRUCT lpCreateStruct) 
{
	if (CDialog::OnCreate(lpCreateStruct) == -1)
		return -1;
	
	CRect rect;
	GetClientRect(&rect);

	// set resizable style
	ModifyStyle(DS_MODALFRAME, WS_POPUP | WS_THICKFRAME);

	// adjust size to reflect new style
	::AdjustWindowRectEx(&rect, GetStyle(), 
						::IsMenu(GetMenu()->GetSafeHmenu()), 
						GetExStyle());

	SetWindowPos(NULL, 0, 0, rect.Width(), rect.Height(), SWP_FRAMECHANGED | 
				SWP_NOMOVE | SWP_NOZORDER | SWP_NOACTIVATE | SWP_NOREPOSITION);

	return 0;
}

void CFindFilesDlg::OnGetMinMaxInfo(MINMAXINFO FAR* lpMMI) 
{
	static bool		bFirstTime = true;
	static CSize	minSize;

	if (IsWindow(GetSafeHwnd()) && IsWindowVisible())
	{
		if (bFirstTime)
		{
			bFirstTime = false;

			// gets the template size as the min track size
			CRect rc;
			GetWindowRect(&rc);
			minSize = rc.Size();
		}
		
		lpMMI->ptMinTrackSize.x = minSize.cx;
		lpMMI->ptMinTrackSize.y = minSize.cy;
	}
}

void CFindFilesDlg::OnSize(UINT nType, int cx, int cy) 
{
	CDialog::OnSize(nType, cx, cy);
	
	if (IsWindow(m_list.GetSafeHwnd()))
	{
		// Move the list window
		CRect rl;
		m_list.GetWindowRect(rl);
		ScreenToClient(rl);
		rl.right = cx - rl.left;
		rl.bottom = cy - rl.left;
		m_list.MoveWindow(rl);
	}
}

void CFindFilesDlg::OnCheckSize() 
{
	BOOL bEnable = (((CButton *)GetDlgItem(IDC_CKSIZE))->GetCheck() == 1);

	GetDlgItem(IDC_EDITMINSIZE)->EnableWindow(bEnable);
	GetDlgItem(IDC_EDITMAXSIZE)->EnableWindow(bEnable);
}

void CFindFilesDlg::OnSearch() 
{
	if (_bSearching)
	{
		_finder.StopSearch();
		return;
	}

	CFileFinder::CFindOpts	opts;

	UpdateData();

	// Set CFindOpts object
	opts.sBaseFolder = m_sBaseFolder;
	opts.sFileMask.Format("*%s*", m_sFileMask);
	opts.bSubfolders = m_bSubFolders;
	opts.FindNormalFiles();

	if (m_bSize)
	{
		opts.dwOptionsFlags |= FIND_SIZE;
		opts.nMinSize = (__int64)m_nMinSize * (__int64)1024;
		opts.nMaxSize = (__int64)m_nMaxSize * (__int64)1024;
	}

	if (!m_sFindText.IsEmpty())
	{
		opts.FindText(m_sFindText);
	}

	// Find files
	if (m_nSearchType == 0)
	{
		m_list.DeleteAllItems();
		SetStatus();
	}

	_bSearching = true;
	GetDlgItem(IDOK)->SetWindowText("Cancel");
	_finder.RemoveAll();
	_finder.Find(opts);
	GetDlgItem(IDOK)->SetWindowText("Search");
	_bSearching = false;

	SetStatus(_finder.GetFileCount());
}

void CFindFilesDlg::FileFinderProc(CFileFinder *pFinder, DWORD dwCode, void *pCustomParam)
{
	CString			sText, sNewFile;
	MSG				msg;
	CFindFilesDlg	*pDlg = (CFindFilesDlg *)pCustomParam;
	int				nListIndex;

	switch (dwCode)
	{
	case FF_FOUND:
		// Update list
		sNewFile = pFinder->GetFilePath(pFinder->GetFileCount() - 1);
		switch (pDlg->m_nSearchType)
		{
		case 0:	// replace
			pDlg->AddFileToList(sNewFile);
			break;

		case 1:	// add
			nListIndex = pDlg->FindInList(sNewFile);
			if (nListIndex == -1) pDlg->AddFileToList(sNewFile);
			break;

		case 2:	// remove
			nListIndex = pDlg->FindInList(sNewFile);
			if (nListIndex != -1) pDlg->m_list.DeleteItem(nListIndex);
			break;
		}

	case FF_FOLDER:
		pDlg->SetStatus(pFinder->GetFileCount(), pFinder->GetSearchingFolder());
	}

	// Process all process messages
	while (PeekMessage(&msg, NULL, 0, 0, PM_REMOVE))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
}

void CFindFilesDlg::AddFileToList(LPCTSTR szFilename)
{
	int		nIndex;
	CPath	path(szFilename);
	__int64	nSize64;
	long	nSize;
	CString	sText;
	CTime	tModified;

	// File name
	nIndex = m_list.InsertItem(m_list.GetItemCount(), path.GetFileName(), 0);

	// File location
	m_list.SetItemText(nIndex, 1, path.GetLocation());

	// File size
	path.GetFileSize(nSize64);
	nSize = (long) (nSize64 / (__int64)1024);
	if (nSize < 10)
		sText.Format("%ld B", nSize64);
	else
		sText.Format("%ld KB", nSize);

	m_list.SetItemText(nIndex, 2, sText);

	// File modified date
	path.GetFileTime(tModified);
	m_list.SetItemText(nIndex, 3, tModified.FormatGmt("%d-%m-%Y %I:%M %p"));
}

int	CFindFilesDlg::FindInList(LPCTSTR szFilename)
{
	int		nIndex;
	bool	bFound;

	for (nIndex = 0; nIndex < m_list.GetItemCount(); nIndex++)
	{
		bFound = (GetListFilename(nIndex).CompareNoCase(szFilename) == 0);
		if (bFound) break;
	}

	return (bFound ? nIndex : -1);
}

CString	CFindFilesDlg::GetListFilename(int nIndex)
{
	return m_list.GetItemText(nIndex, 1) + m_list.GetItemText(nIndex, 0);
}

void CFindFilesDlg::OnCancel() 
{
	if (!_bSearching) CDialog::OnCancel();
}

void CFindFilesDlg::OnBrowse() 
{
	CString		sFolder;
	LPMALLOC	pMalloc;

    // Gets the Shell's default allocator
    if (::SHGetMalloc(&pMalloc) == NOERROR)
    {
        BROWSEINFO bi;
        char pszBuffer[MAX_PATH];
        LPITEMIDLIST pidl;

        bi.hwndOwner = GetSafeHwnd();
        bi.pidlRoot = NULL;
        bi.pszDisplayName = pszBuffer;
        bi.lpszTitle = _T("Select a directory...");
        bi.ulFlags = BIF_RETURNFSANCESTORS | BIF_RETURNONLYFSDIRS;
        bi.lpfn = NULL;
        bi.lParam = 0;

        // This next call issues the dialog box.
        if ((pidl = ::SHBrowseForFolder(&bi)) != NULL)
        {
            if (::SHGetPathFromIDList(pidl, pszBuffer))
            { 
	            // At this point pszBuffer contains the selected path
				sFolder = pszBuffer;
            }

            // Free the PIDL allocated by SHBrowseForFolder.
            pMalloc->Free(pidl);
        }
        // Release the shell's allocator.
        pMalloc->Release();
    }

	GetDlgItem(IDC_EDITROOT)->SetWindowText(sFolder);
}

void CFindFilesDlg::OnDblclkList(NMHDR* pNMHDR, LRESULT* pResult) 
{
	CWaitCursor	waitCursor;
	int			nIndex = m_list.GetSelectionMark();

	ShellExecute(GetSafeHwnd(), NULL, GetListFilename(nIndex), NULL, NULL, SW_SHOW);
	
	*pResult = 0;
}

void CFindFilesDlg::SetStatus(int nCount, LPCTSTR szFolder)
{
	CString sStatus;

	if (szFolder != NULL)
		sStatus.Format("(%d) - %s", nCount, szFolder);
	else
		sStatus.Format("%d items found", nCount);

	GetDlgItem(IDC_STSTATUS)->SetWindowText(sStatus);
}
