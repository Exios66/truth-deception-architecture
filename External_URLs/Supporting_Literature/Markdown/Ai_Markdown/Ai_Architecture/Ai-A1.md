# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

## Citation Information

- **Author(s)**: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou
- **Title**: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- **Journal/Source**: Presented at the 36th Conference on Neural Information Processing Systems (NeurIPS 2022).
- **Publication Year**: 2022
- **DOI/URL**: Not explicitly provided in the snippet, but available through [arXiv](https://arxiv.org/abs/2201.11903).

## Audience

- **Target Audience**: Researchers and practitioners in artificial intelligence, especially those working on natural language processing (NLP), machine learning (ML), and large language models (LLMs).
- **Application**: Implementing chain-of-thought (CoT) prompting to improve reasoning in LLMs for various tasks, including arithmetic, commonsense, and symbolic reasoning.
- **Outcome**: Enhanced reasoning capabilities in LLMs, leading to performance improvements on benchmarks without extensive model fine-tuning.

## Relevance

- **Significance**: Addresses the limitation of standard prompting in reasoning tasks and demonstrates the emergent abilities of LLMs at scale.
- **Real-world Implications**: Facilitates tasks requiring complex reasoning, such as mathematical problem-solving, interactive AI systems, and educational tools.

## Conclusions

- **Takeaways**:
  1. CoT prompting significantly improves the performance of LLMs on reasoning tasks, surpassing fine-tuned models in some cases.
  2. Benefits of CoT are most evident in sufficiently large models (e.g., PaLM 540B).
  3. CoT prompting is versatile and applicable across various reasoning domains.
- **Practical Implications**: CoT can be readily implemented in existing LLMs by providing example prompts, avoiding the need for task-specific fine-tuning.
- **Potential Impact**: Wider application of CoT prompting can make LLMs more robust and capable of solving real-world problems requiring step-by-step reasoning.

## Contextual Insight

- **Abstract in a Nutshell**: This paper explores how CoT prompting, which involves using intermediate reasoning steps in model prompts, enables large LLMs to perform complex reasoning tasks effectively.
- **Abstract Keywords**: [chain-of-thought prompting](https://scholar.google.com/scholar?q=chain+of+thought+prompting), [large language models](https://scholar.google.com/scholar?q=large+language+models), [reasoning tasks](https://scholar.google.com/scholar?q=reasoning+tasks).
- **Gap/Need**: Traditional prompting methods fail on reasoning-heavy tasks, requiring methods like CoT to unlock reasoning capabilities in LLMs.
- **Innovation**: Demonstrates the emergent nature of reasoning abilities with CoT prompting in LLMs and achieves state-of-the-art performance without model fine-tuning.

## Key Quotes

1. "Chain-of-thought reasoning processes are highlighted as a series of intermediate natural language steps leading to the final output."
2. "CoT prompting improves performance on arithmetic, commonsense, and symbolic reasoning benchmarks."
3. "Scaling up model size is a key factor in realizing the benefits of CoT prompting."
4. "CoT prompts serve as interpretable windows into the reasoning of LLMs, aiding debugging and comprehension."
5. "Emergent abilities of LLMs make CoT a valuable addition for enhancing task-solving capabilities."

## Questions and Answers

1. **What is CoT prompting?**
   CoT prompting uses natural language reasoning steps as part of the input prompt to enable LLMs to perform complex reasoning.
2. **Why is CoT prompting important?**
   It overcomes the limitations of standard prompting in reasoning tasks and demonstrates the potential of LLMs for broader applications.
3. **What benchmarks were improved with CoT?**
   GSM8K for math problems, commonsense reasoning tasks like CSQA, and symbolic reasoning benchmarks.
4. **What models benefit most from CoT?**
   Large-scale models like PaLM 540B and GPT-3 175B.
5. **Is CoT resource-intensive?**
   It depends on large-scale models but does not require fine-tuning, making it efficient for deployment.
