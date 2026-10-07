# Modern AI Systems — каркас отчёта

Главный файл: `Tempel-Daniel.tex`. Результат сборки: `Tempel-Daniel.pdf`.
Introduction, PREFACE, все десять тематических глав (2–11) и SUMMARY заполнены.
Перед сдачей необходимы итоговая сборка PDF и проверка полного отчёта.

## Где писать

| Файл | Назначение |
| --- | --- |
| `metadata.tex` | Название, автор, дата, код курса и необязательная программа обучения |
| `preamble.tex` | Общие параметры оформления и APA 7 |
| `frontmatter/cover.tex` | Титульная страница |
| `frontmatter/preface.tex` | Обязательная отдельная PREFACE |
| `chapters/introduction.tex` | Короткое введение вне десяти тем |
| `chapters/01-local-llm-models.tex` | Understanding Local LLM Models — обязательная тема |
| `chapters/02-benchmarks-model-selection.tex` | LLM Benchmarks and Model Selection — обязательная тема |
| `chapters/03-structured-outputs-tool-use.tex` | Structured Outputs, Function Calling and Tool Use |
| `chapters/04-context-engineering-memory.tex` | Context Engineering and Memory |
| `chapters/05-rag-agentic-retrieval.tex` | RAG and Agentic Retrieval |
| `chapters/06-model-context-protocol.tex` | Model Context Protocol — MCP |
| `chapters/07-agents-agent-harnesses.tex` | AI Agents and Agent Harnesses |
| `chapters/08-production-architecture.tex` | Production Architecture for AI Systems |
| `chapters/09-security-sandboxing.tex` | Security and Sandboxing for AI Agents |
| `chapters/10-evaluation-observability-reliability.tex` | Agent Evaluation, Observability and Reliability |
| `chapters/summary.tex` | Обязательная итоговая SUMMARY |
| `references.bib` | Общая база проверенных источников |

Пиши текст после `\label{...}` в соответствующем файле. Не добавляй в главы
`\documentclass`, `\begin{document}` или отдельный список литературы.
Для нового абзаца оставляй пустую строку. Подразделы добавляй по необходимости
через `\section{Descriptive Heading}`: минимум два, с разными названиями.
INTRODUCTION — глава 1; десять тем — главы 2–11; SUMMARY — глава 12.
Числа в именах файлов обозначают номера тем, а не номера глав в отчёте.

## Сборка

Из корневой папки проекта, используя установленный TeX Live:

```powershell
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build Tempel-Daniel.tex
Copy-Item -LiteralPath 'build/Tempel-Daniel.pdf' -Destination 'Tempel-Daniel.pdf'
```

`latexmk` запускает нужные проходы XeLaTeX и Biber. Нужны Arial и пакеты,
перечисленные в `preamble.tex`, в том числе `biblatex-apa`. Пакеты и шрифты
автоматически не устанавливаются. В другом окружении сначала проверь наличие Arial.
После изменения глав повторяй сборку: PDF сам по себе не обновляется.

Главный `.tex` можно редактировать в Codex. Встроенная компиляция Codex рассчитана
на отдельный документ и может не поддерживать внешние файлы глав, шрифты и Biber.
Для этого многофайлового проекта полная сборка выполняется командой выше.

## Ссылки и библиография

Настроены `biblatex`, `style=apa` и `backend=biber`: это основа APA 7,
а не отдельный сертифицированный TAMK-стиль. Особые типы источников сверяй с Guide.
Добавляй только реальные, проверенные записи в `references.bib`.
Список REFERENCES автоматически содержит только цитируемые записи.
Пока источников нет, пустая библиография и предупреждение о ней ожидаемы.

Примеры команд (ключ `source-key` нужно заменить ключом реальной записи):

```latex
\parencite{source-key}             % (Author, year)
\parencite[42]{source-key}         % (Author, year, p. 42)
\parencite[42--44]{source-key}     % (Author, year, pp. 42–44)
\textcite[42]{source-key}          % Author (year, p. 42)
```

Повторяй ссылку в каждом основанном на источнике абзаце. Указывай страницы,
если они есть; разделяй пересказ источника и собственное рассуждение.
Для электронных источников сохраняй дату обращения в `urldate` (YYYY-MM-DD)
и URL; при наличии постоянного идентификатора используй DOI/URN.
Проверь итоговое отображение даты обращения по правилам TAMK для данного типа
источника: стандартный APA может показывать её не во всех случаях.
Не используй `\nocite{*}` для вывода непрочитанных или нецитируемых источников.

## Оформление и границы адаптации

Класс `report`, A4, Arial 12 pt, интервал 1,15, выравнивание по ширине,
поля по 2 см в основной части. Между абзацами 5 pt; отступы у заголовков,
формул и рисунков уменьшены. Главы начинаются с новой страницы,
номера страниц стоят сверху справа. Обложка сохраняет прежние поля шаблона.
Оглавление набрано 11 pt с уменьшенными интервалами между главами,
чтобы все добавленные подразделы помещались на одной странице.
Титульная страница учитывается как первая, но номер на ней скрыт.

Компактный вариант введён по запросу автора. После добавления полноценных схем
для первой темы согласован объём до четырёх страниц с сохранением всего текста.
Он отличается
от TAMK Guide B, где предусмотрены левое поле 4 см и интервал 1,5.
Перед сдачей нужно согласовать эти отклонения или вернуть параметры TAMK
и сократить сам текст. Дальнейшее изменение рисунков может изменить объём.

## Изображения первой главы

Все изображения этой главы хранятся в `images/`:

- `local-llm-inference-pipeline-autoregressive.png` — Figure 1 с Generated token и стрелкой возврата к контексту.
- `local-llm-inference-pipeline.png` — исходная первая схема, сохранённая без изменений.
- `local-llm-inference-pipeline-edit-prompt.txt` — запрос для редактирования Figure 1 встроенным imagegen.
- `model-size-comparison.pdf` — векторный bar chart вместо Table 1, Figure 2.
- `model-size-comparison.png` — PNG-копия графика для просмотра.
- `local-llm-runtime-memory.png` — вторая предоставленная схема, Figure 3.
- `create_model_size_chart.py` — воспроизводимый исходник графика на ReportLab.

Исходные PNG сохранены без изменений. Встроенная подпись «Figure 2» во второй
схеме скрывается параметрами `trim` и `clip` при вставке в LaTeX; подписи
и нумерация всех трёх рисунков формируются документом. Значения графика:
F16 — 14.96 GiB, Q8_0 — 7.95 GiB, Q4_K_M — 4.58 GiB, Q2_K — 2.95 GiB.
Для пересоздания векторного графика запусти `images/create_model_size_chart.py`
в Python с ReportLab; скрипт использует установленный Windows-шрифт Arial.

Основой служит предоставленный `thesis_report_template_2025.docx` и актуальные
разделы TAMK Report Guide, проверенные 27.09.2026. Оригинальное оформление
обложки извлечено из `word/media/image1.emf` этого DOCX и преобразовано в
`assets/tamk-cover.png`. Оно предназначено для этой обложки TAMK.
Название и подзаголовок рабочие; их можно изменить в `metadata.tex`.
Название программы оставлено пустым, поскольку оно не предоставлено.

Это LaTeX-адаптация Word-шаблона для курсового отчёта, а не официальный
LaTeX-шаблон TAMK или обещание побайтово одинаковой вёрстки. COURSE REPORT
заменяет обозначение дипломной работы. Abstract, thesis AI declaration,
glossary и appendices не добавлены автоматически. Требования данного задания
имеют приоритет: PREFACE и SUMMARY включены, INTRODUCTION добавлено для связности.

Таблицу или рисунок сначала объясни в тексте. Подпись таблицы размещай сверху,
рисунка — снизу; чужие материалы сопровождай источником и необходимыми сведениями
о праве использования. В заготовке нет декоративных рисунков внутри глав.
Доступность PDF и альтернативные описания будущих изображений нужно проверить
отдельно, когда появится содержимое; наличие PDF-закладок само по себе её не доказывает.

## Объём перед сдачей

Глава 10, `chapters/09-security-sandboxing.tex`, содержит разделы 10.1–10.3:
least privilege, sandboxing, sensitive resources и prompt injection.
Таблица прав и ограничений оформлена как Table 3. Приложенная схема заменяет
текстовый набросок (теперь Figure 16); оригинал сохранён без изменений в
`images/agent-security-sandboxing.png`. Добавлены два источника OWASP издания 2025;
буквы a/b в ссылках определяются автоматически по порядку библиографии.

Глава 9, `chapters/08-production-architecture.tex`, содержит разделы 9.1–9.3:
model routing, efficient LLM serving и resilient/scalable agent execution.
Figures 14–15: `images/production-architecture.png` и
`images/long-running-task-execution.png`; оригиналы сохранены без изменений.
Добавлены девять источников, включая документацию vLLM для prefix caching.
Недатированные страницы Ray, Temporal и vLLM цитируются с n.d.; дата обращения
06.10.2026 хранится отдельно. Заголовки и основной текст используют British English.

Глава 8, `chapters/07-agents-agent-harnesses.tex`, содержит полный предоставленный
текст: введение и разделы 8.1–8.3 об agent loop, task state, recovery, completion
и делегировании субагентам. Figure 12: `images/agent-loop-harness.png`;
Figure 13: `images/agent-subagent-delegation.png`. Оба оригинала сохранены
без изменений. Прежняя схема `images/agent-subagent-inspection.png` не используется.
Глава ссылается на четыре источника; новый источник о multi-agent research
system оформлен по указанным в статье авторам (Hadfield et al., 2025).
Нумерация последующих рисунков обновится при следующей сборке PDF.

Глава 7, `chapters/06-model-context-protocol.tex`, содержит текст о MCP, роли Host,
клиентах и серверах, интеграции tools и границах протокола. Figures 10–11 хранятся
в `images/mcp-host-client-server.png` и `images/mcp-tool-execution-flow.png`;
оба оригинала сохранены без изменений. Добавлены четыре источника, включая
спецификацию MCP 2026-07-28. Недатированная документация GitHub цитируется с n.d.

Глава 6, `chapters/05-rag-agentic-retrieval.tex`, содержит текст о RAG и agentic
retrieval, сравнительную таблицу retrieval signals и Figure 9. Исходная схема
сохранена без изменений в `images/rag-agentic-retrieval.png`. Шесть источников
добавлены в общую библиографию; для Singh et al. указана версия 1 от 2025 года.

Глава 5, `chapters/04-context-engineering-memory.tex`, содержит текст о context
engineering, history, task state, persistent memory, compaction и prompt caching.
Диаграммы `images/context-builder.png` (Figure 7) и
`images/context-evolution.png` (Figure 8) сохранены без изменений; внешние пустые
поля первой схемы скрываются при вставке в LaTeX. Семь источников добавлены
в общую библиографию; недатированная документация цитируется с n.d.

Глава 4, `chapters/03-structured-outputs-tool-use.tex`, содержит текст о structured
outputs, function calling и tool use, три JSON-примера, последовательность
вызовов и таблицу уровней ошибок. Диаграмма Figure 6 хранится в
`images/tool-execution-architecture.png`; предоставленный PNG сохранён без изменений.
Четыре источника главы включены в общую библиографию.

Глава 3, `chapters/02-benchmarks-model-selection.tex`, содержит предоставленный
текст о benchmarks и выборе модели. Схемы хранятся в `images/`:
`benchmark-evaluation-dimensions.png` (Figure 4) и
`evaluation-result-factors.png` (Figure 5). Обе PNG-копии сохранены без изменений.
Семь источников этой главы включены в общую `references.bib`;
ссылки на главы и разделы формируются автоматически.

- Английский язык; все десять тем, включая первые две обязательные.
- Минимум две содержательные страницы на каждую тему; ориентир 2–2,5 страницы.
- SUMMARY минимум на одну содержательную страницу; отдельная PREFACE и обложка.
- Примерный итоговый объём 25–30 страниц вместе с вводными страницами и источниками.
- Сквозной пример: AI Software Engineering Assistant, исправляющий issue и проверяющий результат.
- Пустые страницы каркаса не подтверждают выполнение требований к объёму.
- Перед сдачей пересобери PDF и проверь ссылки, оглавление, переносы и страницы.
- Итоговое имя файла: `Tempel-Daniel.pdf`.

## Источники требований

- [A — Reading instructions](https://opiskelijanopas.tuni.fi/en/tamk/studying-0/tamks-report-guide/report-guide-reading-instructions)
- [B — Layout and structure](https://opiskelijanopas.tuni.fi/en/tamk/studying-0/tamks-report-guide/report-guide-b-report-layout-structure-and-appendices)
- [C — Tables and figures](https://opiskelijanopas.tuni.fi/en/tamk/studying-0/tamks-report-guide/report-guide-c-tables-figures-and-pictures)
- [D — In-text citations](https://opiskelijanopas.tuni.fi/en/tamk/studying-0/tamks-report-guide/report-guide-d-references-text)
- [E — References](https://opiskelijanopas.tuni.fi/en/tamk/studying-0/tamks-report-guide/report-guide-e-list-references)

Эти ссылки документируют происхождение настройки каркаса; они не добавлены
автоматически в библиографию учебного отчёта.

## Глава 11: оценка и надёжность агента

`chapters/10-evaluation-observability-reliability.tex` содержит три раздела,
формулы cost per successful task, pass@k и pass^k и ссылки на четыре источника.
Схемы сохранены без изменений в `images/assistant-trial-evaluation.png`
(Figure 17) и `images/evaluation-regression-loop.png` (Figure 18).
Они заменяют текстовые наброски из исходного материала.

## Дополнения к обязательным темам

В главу 2 добавлены FP8 (E4M3/E5M2) и обозначения quantization recipes
Q2–Q8, K/S/M, IQ и publisher-specific UD. В главу 3 добавлены MATH и
Chatbot Arena как примеры Reasoning/Math и Human Preference evaluation.
Четыре новых источника включены в общую библиографию.
Интервал между главами в оглавлении уменьшен до 0.4 em; Figure 13
набрана шириной 88% строки, чтобы завершение главы 8 не занимало отдельную страницу.

В главе 2 дополнено объяснение практического значения native low-bit models.
Для компактной вёрстки только внутри этой главы интервал между абзацами
сокращён до 3 pt, интервалы вокруг формул — до 3 pt; Figure 1 имеет ширину
11.5 cm, Figure 3 — 13 cm. Размер шрифта и межстрочный интервал сохранены.
LLM, CI и nDCG@k расшифрованы при первом употреблении; в Preface добавлен
AI acknowledgement. После этих последних изменений PDF не пересобирался
по просьбе автора; итоговое число страниц требует проверки при следующей сборке.
