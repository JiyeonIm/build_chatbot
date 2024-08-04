from llama_cpp import Llama
import datetime
from DB import connect_db

def write_text(lines):
    file_path = "output.txt"
    with open(file_path, "a", encoding='utf-8') as f:
        for key, value in lines.items():
            f.write(f"{key}: {value}\n")
        f.write("\n")


def get_response(question):
    start_time = datetime.datetime.now()
    print(start_time)
    llm = Llama(
        model_path="llama3-8b-instruct-Q5_K_M.gguf",
        n_ctx=4096,
        n_threads=4,
    )

    test = f"Q: {question} A: "
    output = llm(test, max_tokens=200, stop=["Q:", "\n"], echo=True)
    answer = output['choices'][0]['text'].split(test)[-1]
    created_time = datetime.datetime.fromtimestamp(output['created'])
    print(created_time)

    latency = created_time - start_time
    print(latency)
    lines = {"question": question, "answer": answer, "latency": f"{latency.total_seconds()} seconds."}
    
    write_text(lines)
    connect_db(lines)

    # print("answer: ", answer)

    return answer

if __name__ == '__main__':
    question = "What are names of the planet in the solar system?"
    answer = get_response(question)