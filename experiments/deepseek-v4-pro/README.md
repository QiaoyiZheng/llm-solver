# DeepSeek V4 Pro experiment

Reserved isolated layout for the `deepseek-v4-pro` certificate experiment. Its
future runner must use the shared certificate response schema; there is no
status-only baseline task. It must compare the verdict first and run certificate
verification only for a correct verdict.

API configuration is in `config/api.json`. It loads the secret from the
repository-root `api-key` file, with `DEEPSEEK_API_KEY` as a fallback. The
secret itself must never be copied into a run directory or log.
