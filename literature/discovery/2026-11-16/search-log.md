# Search log — discovery round 1
Date: 16/11/2026 (Asia/Ho_Chi_Minh / UTC+7).
Status: exploratory discovery; not a locked systematic review, not PRISMA counts.

## search_T1.json
Source: web search; returned ranked results preserved in raw log. The service does not provide a complete database hit count.
- Q1: museum cultural heritage question answering dataset benchmark text retrieval survey
- Q2: cultural heritage museum retrieval augmented generation chatbot evaluation benchmark

## search_T2.json
Source: web search; returned ranked results preserved in raw log. The service does not provide a complete database hit count.
- Q1: retrieval augmented generation benchmark citation evidence attribution ALCE RAGTruth RAGChecker
- Q2: evidence sufficiency answer abstention benchmark RAG NoMIRACL RGB

## search_T3.json
Source: web search; returned ranked results preserved in raw log. The service does not provide a complete database hit count.
- Q1: Self-RAG Corrective Retrieval Augmented Generation adaptive retrieval paper
- Q2: GraphRAG multi hop question answering HippoRAG evidence retrieval paper

## search_T4.json
Source: web search; returned ranked results preserved in raw log. The service does not provide a complete database hit count.
- Q1: RAG citation claim verification attribution ReClaim RARR FActScore paper
- Q2: Correctness is not Faithfulness retrieval augmented generation attributions citation paper

## search_T5.json
Source: web search; returned ranked results preserved in raw log. The service does not provide a complete database hit count.
- Q1: Sufficient Context retrieval augmented generation selective answering abstention paper
- Q2: retrieval augmented generation conflicting sources abstention CONFLICTS DRAGged benchmark

## search_T6.json
Source: web search; returned ranked results preserved in raw log. The service does not provide a complete database hit count.
- Q1: Vietnamese retrieval augmented generation question answering benchmark ViRAG ViMRC
- Q2: multilingual RAG cross language evidence consistency cultural bias benchmark MIRACL BERGEN

## search_seeds.json
Source: web search; returned ranked results preserved in raw log. The service does not provide a complete database hit count.
- Q1: MuseumQA Amarna VISCOUNTH cultural heritage benchmark question answering
- Q2: "SEA-VQA" "VaseVQA" "VQArt-Bench"
- Q3: "LongHisDoc" "CIDOC-QA"
- Q4: "RAGAS" "ARES" retrieval augmented generation evaluation
- Q5: "MIRACL" "BERGEN" multilingual retrieval augmented generation
- Q6: "RARR" "FActScore" "RAGTruth"

## search_exact.json
Source: web search; returned ranked results preserved in raw log. The service does not provide a complete database hit count.
- Q1: "MuseumQA: A Fine-Grained Question Answering Dataset"
- Q2: "ARES: An Automated Evaluation Framework"
- Q3: "RAGAS: Automated Evaluation"
- Q4: "RARR: Researching and Revising"
- Q5: "FActScore: Fine-grained Atomic"
- Q6: "MIRACL: A Multilingual Retrieval Dataset"
- Q7: "BERGEN" "Benchmarking Retrieval"
- Q8: "Making Retrieval-Augmented Language Models Robust" "NoMIRACL"

## OpenAlex access check
Query: cultural heritage question answering; per-page=2.
URL: https://api.openalex.org/works?search=cultural%20heritage%20question%20answering&per-page=2
HTTP 503. Response: Anonymous search is paused while the search cluster recovers from heavy load; free API key suggested by provider. No result records were imported.

## Metadata lookup
Crossref exact-title lookups are stored as raw/crossref_*.json. Top 3 matches requested; only title similarity >=0.94 accepted, with response and match score kept. These are bibliographic enrichment, not additional formal database searches.

## Prior seeds
Ten canonical seed URLs from the earlier user/Elicit discovery discussion were rechecked against source metadata. These are explicitly labeled PRIOR_SEED, not counted as newly found formal search records.

## Limits
No formal source/IC/EC protocol was locked for this round. No database-wide completeness claim; no systematic citation snowball was completed. No full-text evidence extraction, relevance screening, quality assessment, or human crosscheck was performed.
