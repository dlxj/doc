



```js
SELECT order_id, order_date, json_extract(customer, '$.name') AS cusName,json_extract(customer, '$.city') AS cusCity FROM read_json_auto('orders.json')
```



```
SELECT sum(od.quantity*od.price) amount
FROM read_json_auto('orders.json') AS o,
LATERAL UNNEST(o.order_details) AS t(od),
LATERAL UNNEST([od.product]) AS t(p)
WHERE p.category = 'Electronics'
```



```

SELECT
    o.order_id, 
    LIST_FILTER(o.order_details, x -> x.product.category = 'Electronics') AS order_details
FROM read_json_auto(orders.json') AS o
WHERE 
    ARRAY_LENGTH(LIST_FILTER(o.order_details, x -> x.product.category = 'Electronics')) > 0
    AND SUM(
        LIST_FILTER(o.order_details, x -> x.product.category = 'Electronics') -> 
            (x -> x.price * x.quantity)
    ) > 200;

```





# parquet 优缺点



Parquet 是一种列式存储格式，而 DuckDB 是一个进程内 OLAP（联机分析处理）数据库。两者结合通常被认为是数据分析领域的“黄金搭档”。

以下是在 DuckDB 中使用 Parquet 格式的主要优缺点：

**优点 (Pros)**

1. 极高的查询性能 (Columnar Synergy)
   
   - 列式对齐 ：DuckDB 的内部执行引擎是向量化（Vectorized）和列式的，这与 Parquet 的物理存储布局完美契合。
   - 零拷贝/直接读取 ：DuckDB 可以直接在 Parquet 文件上运行查询，而无需先将数据“导入”或复制到数据库内部存储中。
   - 投影下推 (Projection Pushdown) ：如果你的查询只涉及表中的几列（例如 SELECT col_a FROM table ），DuckDB 只会从 Parquet 文件中读取 col_a 的数据块，极大减少 I/O。
2. 智能过滤 (Filter Pushdown)
   
   - DuckDB 利用 Parquet 文件头中的元数据（如 Row Groups 的 min/max 统计信息）来跳过无关的数据块。
   - 例如查询 WHERE age > 30 ，如果某个 Row Group 的 max_age 是 25，DuckDB 会完全跳过读取该块。
3. 存储效率与压缩
   
   - Parquet 针对每一列的数据类型使用特定的编码和压缩算法（如 Snappy, Zstd, RLE, Dictionary Encoding）。
   - 相比 CSV 或 JSON，Parquet 文件通常更小，不仅节省磁盘空间，还能减少读取时的磁盘 I/O 带宽压力。
4. 生态互操作性
   
   - Parquet 是通用的标准格式。你可以在 Python (Pandas/Polars)、Spark、AWS S3 等环境中生成 Parquet 文件，然后直接用 DuckDB 查询，无需转换格式。
5. 支持复杂数据类型
   
   - 相比 CSV，Parquet 原生支持嵌套结构（Lists, Structs, Maps），DuckDB 对这些复杂类型的支持也越来越完善。



**缺点 (Cons)**

1. 不支持高效的更新/删除 (Immutability)
   
   - 最大痛点 ：Parquet 文件设计为“一次写入，多次读取”（Write-Once-Read-Many）。
   - 如果你需要修改或删除一行数据，通常需要重写整个文件（或至少重写相关的 Row Group）。
   - 不适合 OLTP ：如果你的场景需要频繁的单行插入、更新或事务处理，原生 Parquet 并不适合（DuckDB 自己的 .db 格式更适合这种混合负载）。
2. 小文件问题 (Small File Problem)
   
   - 如果数据被分割成成千上万个非常小的 Parquet 文件（例如每个文件只有几 KB），读取性能会急剧下降。
   - 这是因为打开文件、解析元数据的开销超过了读取实际数据的开销。DuckDB 处理单个大文件（或适量的大文件）的效率远高于处理海量小文件。
3. 写入开销
   
   - 生成 Parquet 文件需要 CPU 进行编码和压缩。与简单的追加写入 CSV 相比，写入 Parquet 会消耗更多的 CPU 资源和时间（尽管这通常是值得的，因为读取速度会快得多）。
4. 不适合流式追加
   
   - 由于 Parquet 文件包含尾部元数据（Footer），你不能像写日志一样简单地通过 cat 命令把新数据追加到文件末尾。必须由专门的库来处理文件的合并或生成新文件。



**总结建议**

- 使用场景 ：历史数据分析、数据湖查询、一次写入多次读取的报表生成、跨工具数据交换。
- 避免场景 ：需要实时更新用户状态、高频事务交易系统、流式日志的实时追加写入（除非分批次写入）。
在 DuckDB 中，最常见的模式是：使用 DuckDB 的内部格式（ .db ）处理热数据或需要更新的数据，定期将冷数据或归档数据导出为 Parquet 以节省空间并供其他工具使用。





# 替换 Json 合适吗

如果你的目标是 替换 JSON 数据格式 （特别是用于存储、日志记录或数据交换的 JSON），使用 DuckDB 是 非常合适 的，甚至可以说是目前市面上 性价比最高 的方案之一。

以下是为什么用 DuckDB（及其原生格式或配合 Parquet）替换 JSON 是一个巨大升级的原因：



1. 存储空间：从“膨胀”到“极致压缩”
- JSON ：是基于文本的，非常啰嗦。每个字段名在每一行都要重复一遍（例如 {"id": 1, "name": "a"} , {"id": 2, "name": "b"} ... "id" 和 "name" 被存储了无数次）。
- DuckDB ：
  - 它是列式存储，相同的字段名只存一次元数据。
  - 它会自动检测每一列的最佳压缩算法。
  - 效果 ：通常能将 JSON 文件的大小压缩 5倍到 20倍 。10GB 的 JSON 日志转入 DuckDB 可能变成几百 MB。




2. 读取性能：告别“解析地狱”
- JSON ：计算机处理 JSON 最慢的步骤不是“读取磁盘”，而是 解析（Parsing） 。CPU 必须逐个字符扫描 { , } , : , " 才能理解数据结构。这是极度消耗 CPU 的。
- DuckDB ：数据是二进制格式，且按列排列。
  - 无需解析文本。
  - 可以直接将数据块 memcpy 到内存中。
  - 效果 ：查询速度通常比直接处理 JSON 快 10倍到 100倍 。



3. 查询能力：SQL vs. 脚本循环
- JSON ：如果你想从 100 万行 JSON 中找出 status: "error" 的记录并按 date 聚合，你通常需要写 Python/Node.js 脚本或用 jq 工具，这很慢且容易出错。
- DuckDB ：
  - 你可以直接用 SQL： SELECT date, count(*) FROM logs WHERE status = 'error' GROUP BY date 。
  - 即使数据结构很复杂（嵌套），DuckDB 也支持 struct 和 list 类型，或者直接保留为 JSON 类型列进行查询。



4. 灵活性：DuckDB 对 JSON 的原生支持
DuckDB 有一个非常强大的特性： 它不强迫你立刻定义完美的 Schema 。

如果你的 JSON 字段经常变（这也是大家爱用 JSON 的原因），DuckDB 有两种处理方式：

1. 自动推断（Auto Detection） ：它会扫描 JSON 文件，自动猜出最合理的表结构。
   ```
   SELECT * FROM read_json_auto('data.json');
   ```
2. JSON 数据类型 ：你可以把原本复杂的嵌套部分直接存为一个 JSON 类型的列，既享受了压缩，又能用 JSON 函数查询。
   ```
   -- 即使 data 列是复杂的嵌套 JSON，也能极速查询
   SELECT data->>'user_id' FROM my_table;
   ```
什么时候 不建议 替换 JSON？
虽然 DuckDB 很强，但如果你的场景是以下几种，保留 JSON 可能更好：

1. 前端直接消费 ：如果数据是直接发给 Web 浏览器或移动端 App 的 API 响应，JSON 是标准，DuckDB 格式浏览器读不懂。
2. 配置文件 ：如果文件需要人工用记事本打开、阅读和修改（如 config.json ），不要换。
3. 单条记录的高频读写 ：如果你是用作 Key-Value 存储（像 Redis 或 MongoDB 那样），按 ID 频繁存取单条记录，DuckDB 不太适合（它是为批量分析设计的）。
最佳实践建议
如果你决定替换，推荐的路径是：

原始 JSON -> [DuckDB 清洗/转换] -> Parquet 文件

这样做的好处是：

- Parquet 是压缩后的二进制，保留了列式优势。
- DuckDB 可以秒级查询 Parquet。
- 如果以后你需要把数据给 Spark、Pandas 或 ClickHouse 用，Parquet 是通用货币，大家都能读，而 DuckDB 的 .db 文件只有 DuckDB 能读。





# 存嵌入向量合适吗



非常合适，尤其是在中小规模（百万级以下）的数据集场景下。

DuckDB 最近在向量存储和检索领域非常火，因为它通过**暴力计算（Brute-force）**实现了惊人的性能，且不需要复杂的索引维护。

以下是 DuckDB 作为向量数据库的详细分析：




1. 核心优势：简单且强大的“精确搜索”
主流向量数据库（如 Milvus, Pinecone, Faiss）通常使用 ANN（近似最近邻） 算法。为了速度，它们牺牲了一点精度，并且需要构建庞大的 HNSW 索引，这很占内存且维护麻烦。

DuckDB 的策略不同：

- 基于 SIMD 的暴力扫描 ：DuckDB 利用现代 CPU 的指令集（AVX-512 等）并行计算向量距离。
- 无需索引 ：它不需要预先建立复杂的向量索引。这意味着你可以随时插入数据，随时查询，没有“重建索引”的开销。
- 精确结果 ：因为是全表扫描，它返回的是数学上 绝对精确 的最近邻（KNN），而不是近似值。
性能表现 ：
在 100 万条 768 维（OpenAI Embedding 标准）向量的数据集上，DuckDB 的全表扫描通常能在 0.1秒 ~ 0.5秒 内完成。对于大多数 RAG（检索增强生成）应用来说，这个延迟完全可以接受。




2. 原生支持的数据类型
DuckDB 有专门的 ARRAY 类型，非常适合存向量：

```
-- 创建一个存 3 维向量的表
CREATE TABLE embeddings (
    id INTEGER,
    text VARCHAR,
    vec FLOAT[3]  -- 固定长度的数组，存储效率极高
);

-- 插入数据
INSERT INTO embeddings VALUES (1, 'apple', [0.1, 0.5, 0.9]);
INSERT INTO embeddings VALUES (2, 'banana', [0.2, 0.4, 0.8]);

-- 向量搜索（余弦相似度）
-- 查找与 [0.1, 0.5, 0.9] 最相似的前 3 个结果
SELECT text, array_cosine_similarity(vec, [0.1, 0.5, 0.9]::FLOAT[3]) as score
FROM embeddings
ORDER BY score DESC
LIMIT 3;
```



3. “混合查询”（Hybrid Search）的王者
这是 DuckDB 相比专用向量数据库最大的优势。

在实际业务中，你很少只做纯向量搜索，通常需要结合元数据过滤。例如：“ 查找最近 7 天内、分类为‘财经’且与这句话语义相似的新闻 ”。

- 专用向量库 ：元数据过滤通常较弱（Pre-filter 或 Post-filter），性能不稳定。
- DuckDB ：它本身就是最强的 SQL 分析引擎。
  ```
  SELECT text, array_cosine_similarity(vec, query_vec) as score
  FROM documents
  WHERE category = 'finance'       -- 极速的列式过滤
    AND date > '2023-01-01'        -- 标准 SQL 过滤
  ORDER BY score DESC
  LIMIT 5;
  ​``` DuckDB 会先利用列式存储的优势快速过滤掉不满足 WHERE 条件的行，只对剩下的行计算向量距离，速度飞快。
  ```



4. 什么时候 不合适？
尽管 DuckDB 很强，但在以下场景请慎用：

1. 超大规模数据（> 500万向量） ：
   - 当数据量达到千万级时，暴力扫描会变得太慢（可能需要几秒钟）。这时候必须用 HNSW 索引，而 DuckDB 目前的原生索引支持不如专用库成熟（虽然有 vss 扩展，但还在早期阶段）。
2. 高并发实时查询 ：
   - DuckDB 是单机进程内的，不适合每秒几千次（QPS > 1000）的并发查询请求。它更适合分析或低频高吞吐的 RAG。
3. 频繁的单点更新 ：
   - 和之前提到的 Parquet 一样，DuckDB 不喜欢频繁修改单行向量。它喜欢批量写入。


总结
- 推荐场景 ：个人知识库（Obsidian/Notion 插件）、本地 RAG 应用、数据分析师的语义搜索工具、离线数据清洗管道。
- 替代方案 ：如果你的数据量真的很大（千万级），或者需要极高的在线并发，请使用 Qdrant 、 Milvus 或 pgvector （PostgreSQL 插件）。



# 全文检索

```

fts和vss插件以及vsssentence-transformers

```







