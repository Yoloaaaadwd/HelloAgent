**Chapter04**  
.env文件原名直接commit 应该会被git忽略，所以当时后面有.env copy 这样的一个文件名，导致程序识别不出来。  
**Chapter07**
.env文件中只要有别的后缀，程序其实都无法识别，例如.env.example  
要注意的是，要看主程序中缺少了什么变量，在.env中进行配置，例如MODELSCOPE_API_KEY，虽然和LLM_API_KEY的值一样，但因为程序中用的前者，所以需要添加上。  
llm创建实例指定了provider才能调用成功。
# 创建LLM实例
```python
llm = HelloAgentsLLM(provider="modelscope")
```


