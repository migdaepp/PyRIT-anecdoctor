# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: pyrit-312
#     language: python
#     name: python3
# ---

# %% [markdown]
# # OpenAI Completions - optional
#
# Before you begin, ensure you are setup with the correct version of PyRIT and have the applicable secrets configured as described [here](../../setup/populating_secrets.md).
#
# Once you are configured, then you will be able to get completions for your text.

# %%
from pyrit.common import IN_MEMORY, initialize_pyrit
from pyrit.orchestrator import PromptSendingOrchestrator
from pyrit.prompt_target import OpenAICompletionTarget

initialize_pyrit(memory_db_type=IN_MEMORY)

# Note that max_tokens will default to 16 for completions, so you may want to set the upper limit of allowed tokens for a longer response.
target = OpenAICompletionTarget(max_tokens=2048)

orchestrator = PromptSendingOrchestrator(objective_target=target)
response = await orchestrator.send_prompts_async(prompt_list=["Hello! Who are you?"])  # type: ignore
await orchestrator.print_conversations_async()  # type: ignore
