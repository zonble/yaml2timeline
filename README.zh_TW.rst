yaml2timeline
=============

.. note::

   **本專案已停止維護，視為歷史遺留（Legacy）專案。**

   原因如下：

   - 本專案撰寫於 2013 年，目標環境為 Python 2，而 Python 2 已於 2020 年 1 月正式停止支援（End-of-Life）。
   - 依賴套件 ``pycli`` 已停止維護，且與現代 Python 不相容。
   - 程式碼中 ``yaml.load()`` 在未指定 ``Loader`` 的情況下使用，屬於不安全的呼叫方式，在目前所有主流版本的 PyYAML 中均會引發警告或錯誤。
   - 所產生 HTML 中使用的 Google Charts JavaScript API 端點（``jsapi?autoload=…``）已被 Google 棄用。
   - 本專案不計劃進行任何主動開發或錯誤修正。

   若您需要類似工具，建議以現代 Python 3 重新實作，並改用 ``click`` 或 ``argparse``、最新版 ``PyYAML``，以及目前的 Google Charts loader（``https://www.gstatic.com/charts/loader.js``）。

- 楊維中 a.k.a zonble
- zonble {at} gmail {dot} com
- 2013/12/20

*yaml2timeline* 是一套在 KKBOX 內部所使用的專案管理工具，使用 Python 語
言開發。這個工具可以將 YAML 所定義的專案進度，輸出成 HTML 格式的專案進
度圖。在 HTML 檔案中，我們則使用 Google 提供的 Google Charts API 繪製專
案進度。

我們在 KKBOX 裡的工作流程是，我們會將這份檔案放在一個內部 git
repository 中，讓所有與專案有關的人都可以編輯；輸出成 HTML 之後，則會用
一面大電視顯示 HTML 內容，這樣只要經過電視前的人，都可以對每個專案下有
多少工作、預計什麼時候完成、是否還有餘裕承擔更多的工作…都一目了然。

安裝
----

在終端機下，使用 git clone 取得本專案的程式碼

``git clone https://github.com/zonble/yaml2timeline.git``

然後輸入以下指令安裝：

``[sudo] python setup.py install``

使用方式
--------

這是一個簡單的命令列工具，使用時，只要在命令列下輸入以下指令即可

``yaml2timeline <輸入 YAML 檔名> <輸出 HTML 檔名>``

文件格式
--------

原始 YAML 的格式大概如下：

::

	<專案 1>:
	- {title: <工作 1>, begin: 2013-12-01, end: 2013-12-30}
	- {title: <工作 2>, begin: 2013-12-08, end: 2014-01-08}
	<專案 2>:
	- {title: <工作 1>, begin: 2013-12-01, end: 2013-12-30}
	- {title: <工作 2>, begin: 2013-12-08, end: 2014-01-08}

經過轉換之後，就可以得到如以下的成品：

.. image:: https://raw.github.com/zonble/yaml2timeline/master/sample/sample.png

希望您喜歡這套工具！
