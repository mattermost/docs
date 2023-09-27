..  _i18n:

Chinese, Japanese and Korean search
======================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Enabling search for Chinese, Japanese and Korean (CJK) requires special configuration, since these languages do not contain spaces.

- See `database requirements documentation </install/software-hardware-requirements.html>`__ for how to set up search for these languages.

.. contents::
    :backlinks: top

Below is additional information on how to configure the database for different languages.

中文 / Chinese
--------------

尽管在 Mattermost 8.0 更新后，官方推荐为了更好的性能请使用 PostgreSQL 作为后端数据库。

但就目前而言，使用 MySQL 能够更容易的实现中文语言的全文搜索功能，在妥善配置 ngram 后，根据官方数据库构造重新生成索引即可达成。
具体的操作方式，可参考： `Cannot search CJK contents <https://github.com/mattermost/mattermost/issues/2033#issuecomment-182336690>`__。

有关 PostgreSQL 的配置方式，请参考以下流程：

配置 SCWS
~~~~~~~~~~

.. code:: bash

    # 取得 SCWS 代码
    wget http://www.xunsearch.com/scws/down/scws-1.2.3.tar.bz2
    # 解压缩
    tar xvjf scws-1.2.3.tar.bz2
    # 进入解压后的目录
    cd scws-1.2.3
    # 执行配置脚本、编译并安装
    ./configure --prefix=/usr/local/scws ; make ; make install
    
    # 可选：检查文件是否存在
    ls -al /usr/local/scws/lib/libscws.la
    /usr/local/scws/bin/scws -h
    # 可选：将词典安装在 /usr/local/scws/etc 中
    cd /usr/local/scws/etc
    wget http://www.xunsearch.com/scws/down/scws-dict-chs-gbk.tar.bz2
    wget http://www.xunsearch.com/scws/down/scws-dict-chs-utf8.tar.bz2
    tar xvjf scws-dict-chs-gbk.tar.bz2
    tar xvjf scws-dict-chs-utf8.tar.bz2

配置 Zhparser
~~~~~~~~~~~~~~

.. code:: bash

    # 下载 Zhparser 源代码
    git clone https://github.com/amutu/zhparser.git
    # 进入下载后的目录
    cd zhparser
    # 编译并安装
    SCWS_HOME=/usr/local/scws make && make install

.. note::

    自 Mattermost 6.0 起，官方已不再使用 mattermost/mattermost-prod-db 作为数据库镜像，你可以直接使用安装在服务器上的 PostgreSQL 数据库，或者使用 PostgreSQL 官方的 Docker 镜像。

    如果使用 Docker 镜像作为数据库，可以预先执行以下命令，安装依赖（请根据实际的 PostgreSQL 版本选择）。

    .. code:: bash

        # 更新本地缓存
        apt update
        # 配置 SCWS 时需要的依赖
        apt install wget make gcc
        # 配置 Zhparser 时需要的依赖
        apt install git postgresql-server-dev-13

创建 extension 并增加解析配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sql

    -- 创建 extension
    CREATE EXTENSION zhparser
    -- 创建 text search configuration
    CREATE TEXT SEARCH CONFIGURATION simple_zh_cfg (PARSER = zhparser);
    -- 配置 token mapping
    ALTER TEXT SEARCH CONFIGURATION simple_zh_cfg ADD MAPPING FOR n,v,a,i,e,l WITH simple;    

更新 PostgreSQL 配置
~~~~~~~~~~~~~~~~~~~~~

将 postgresql.conf 中的 default_text_search_config 的值更改为 simple_zh_cfg。

更改后，需要重启数据库方可生效。

.. note::

    配置完成后，需根据 Mattermost 官方仓库中的 SQL 建表语句重新创建索引，方可正式启用中文语言的全文搜索功能。

    未尽事宜，可以参考以下链接：

    - `SCWS 官方文档 <http://www.xunsearch.com/scws/docs.php>`__
    - `Zhparser 官方文档 <https://github.com/amutu/zhparser/blob/master/README.md>`__
    - `Mattermost 建表语句 <https://github.com/mattermost/mattermost/tree/master/server/channels/db/migrations/postgres>`__

日本語 / Japanese
-----------------

日本語翻訳の改善は大歓迎です。自由に変更していただいて結構です。

検索設定
~~~~~~~~~

Mattermost で日本語検索をするためにはデータベースの設定変更が必要です

- `MySQL </install/requirements.html#database-software>`__

- `Postgres <https://github.com/mattermost/mattermost/issues/2159#issuecomment-206444074>`__

日本語(CJK)検索設定のドキュメントの改善にご協力ください

ガイド
~~~~~~

Qiita上で Mattermost のインストールおよび構成のガイドを提供しています。詳細については、`こちら <http://qiita.com/tags/Mattermost>`_ をご覧ください。

한국어 / Korean
---------------

이 문제에 대한 논의는 이 `이슈 <https://github.com/mattermost/mattermost/issues/2033>`_ 에서 시작되었습니다.

한국어 버전 이용 시 문제점을 발견하면 `Localization 채널 <https://community.mattermost.com/core/channels/localization>`__ 또는 `한국어 채널 <https://community.mattermost.com/core/channels/i18n-korean>`__ 에서 의견을 제시할 수 있습니다.

검색을 위한 데이터베이스 설정
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PostgreSQL: PostgreSQL 데이터베이스에서는 따로 설정이 필요하지 않습니다.

MySQL: MySQL에서는 전문 검색(Full-text search) 기능에 제한이 있기 때문에 추가적인 작업이 필요합니다.

MySQL 해결 방법
~~~~~~~~~~~~~~~~~

1. `n-gram parser <https://mysqlserverteam.com/innodb-%EC%A0%84%EB%AC%B8-%EA%B2%80%EC%83%89-n-gram-parser/>`__ 를 이용하기 위해서는 MySQL의 버전이 5.7.6 이상이어야 합니다.

2. MySQL의 구성 파일에서 n-gram의 최소 토큰 크기를 다음과 같이 설정합니다.

.. code:: sql

    [mysqld]
    ft_min_word_len = 2
    innodb_ft_min_word_len = 2

3. 데이터베이스를 재시작합니다. (이 과정은 반드시 필요합니다.)

4. 일부 테이블의 전문 검색 색인을 다음과 같이 재구성합니다.

- 게시물 검색을 위한 설정 ( `참조 <https://github.com/mattermost/mattermost/issues/2033#issuecomment-182336690>`__ )

.. code:: sql

    DROP INDEX idx_posts_message_txt ON Posts;
    CREATE FULLTEXT INDEX idx_posts_message_txt ON Posts (Message) WITH PARSER ngram;

- 해시 태그 검색을 위한 설정 ( `참조 <https://github.com/mattermost/mattermost/pull/4555>`__ )

.. code:: sql

    DROP INDEX idx_posts_hashtags_txt ON Posts;
    CREATE FULLTEXT INDEX idx_posts_hashtags_txt ON Posts (Hashtags) WITH PARSER ngram;

- 사용자 검색을 위한 설정

  ``Users.idx_users_txt_all`` 과 ``Users.idx_users_names_all`` 을 n-gram 없이 재구성합니다.
