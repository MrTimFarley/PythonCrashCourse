from pathlib import Path

what_i_learned = Path("learning.txt").read_text()
print(what_i_learned)

what_i_learned = what_i_learned.replace("learned", "studied")
print(what_i_learned)
Path("learning_python.txt").write_text(what_i_learned)

