
from agents.planner_agent import PlannerAgent
from agents.coding_agent import CodingAgent
from agents.review_agent import ReviewAgent
from agents.testing_agent import TestingAgent
from agents.memory_agent import MemoryAgent


class AIAgentSystem:
    def __init__(self):
        self.planner = PlannerAgent()
        self.coder = CodingAgent()
        self.reviewer = ReviewAgent()
        self.tester = TestingAgent()
        self.memory = MemoryAgent()

    def execute(self, requirement: str):
        tasks = self.planner.run(requirement)

        results = []

        for task in tasks:
            code = self.coder.run(task)

            review_result = self.reviewer.run(code)
            test_result = self.tester.run(code)

            self.memory.save(task, code)

            results.append({
                "task": task,
                "code": code,
                "review": review_result,
                "test_pass": test_result
            })

        return results


if __name__ == "__main__":
    system = AIAgentSystem()

    result = system.execute("开发一个用户登录系统")

    for item in result:
        print("\n====================")
        print("任务:", item["task"])
        print("代码:", item["code"])
        print("评审:", item["review"])
        print("测试是否通过:", item["test_pass"])
