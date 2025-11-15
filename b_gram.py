import collections

# 示例语料库，与上方案例讲解中的语料库保持一致
corpus = "datawhale agent learns datawhale agent work"
tokens = corpus.split()
total_tokens = len(tokens)

# --- 第一步：计算 P(agent) ---
count_agent = tokens.count('agent')
p_agent = count_agent / total_tokens
print(f"第一步: P(datawhale) = {count_agent}/{total_tokens} = {p_agent:.3f}")

# --- 第二步：计算 P(work|agent) ---
# 先计算 bigrams 用于后续步骤
bigrams = zip(tokens, tokens[1:])
bigram_counts = collections.Counter(bigrams)
count_agent_work = bigram_counts[('agent', 'work')]
# count_agent 已在第一步计算
p_work_given_agent = count_agent_work / count_agent
print(f"第二步: P(work|agent) = {count_agent_work}/{count_agent} = {p_work_given_agent:.3f}")



# --- 最后：将概率连乘 ---
p_sentence = p_agent * p_work_given_agent 
print(f"最后: P('datawhale agent learns') ≈ {p_agent:.3f} * {p_work_given_agent:.3f}  = {p_sentence:.3f}")
