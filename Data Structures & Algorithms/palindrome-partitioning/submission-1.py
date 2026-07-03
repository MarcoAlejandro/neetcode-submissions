class Solution:
    

    def _explore(self, stack: list, suffix: str, answers: list) -> None:
      if not suffix:
        if all(
          map(
            lambda e: e == e[::-1],
            stack
          )
        ):
          answers.append(stack)
        return 
      
      self._explore(
        stack[:-1] + [stack[-1] + suffix[0]],
        suffix[1:],
        answers
      )
      self._explore(
        stack + [suffix[0]],
        suffix[1:],
        answers
      )

    
    def partition(self, s: str) -> List[List[str]]:
        if not s:
          return []
        answers = []
        self._explore([s[0]], s[1:], answers)
        return answers
