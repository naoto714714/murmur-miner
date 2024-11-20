# MurmurMiner
## 概要
- 音声ファイルを文字起こし・要約してテキストファイルで出力する

- `input_audios`に要約したい音声ファイルを置く(複数ファイル可)
  - 入力可能なファイル形式：`.mp3`, `.wav`, `.m4a`

- システムを実行すると、`output_summaries`に`.txt`形式で要約が出力される

### 注意点
- **Perplexity AIのAPIキーが必須**

- Dockerイメージの容量がかなり大きい(約6GB)

## 使い方
1. `input_audios`に要約したい音声ファイルを置く

2. 以下のコマンド(もしくは手動)で、以下の`.env`ファイルを作成
    ```shell
    $ echo 'API_TOKEN="<PerplexityのAPIキー>"' > .env
    ```
    `.env`
    ```
    API_TOKEN="APIキー"
    ```

3. ビルド
   ```shell
   $ docker build -t murmur .
   ```

4. 実行
   ```shell
   $ docker run --rm murmur
   ```

## 使用した技術
- パッケージ管理：[uv](https://docs.astral.sh/uv/guides/integration/docker/)

- 無音区間除去：[silero-vad](https://github.com/snakers4/silero-vad)

- 文字起こし：[kotoba-whisper-v2.0 ](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0)

- 要約：[Perplexity API](https://docs.perplexity.ai/api-reference/chat-completions)
