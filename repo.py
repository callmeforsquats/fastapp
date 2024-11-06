from sqlalchemy import select
from databasa import new_secc, TaskTable
from models import TaskAdd, TaskRead


class TaskRepos:
    @classmethod
    async def add(cls,task:TaskAdd):
        async with new_secc() as sess:
            task_dict=task.model_dump()
            task=TaskTable(**task_dict)
            sess.add(task)
            await sess.flush()
            await sess.commit()
            return task.id

    @classmethod
    async def find(cls) ->list[TaskRead]:
        async with new_secc() as sess:
            query=select(TaskTable)
            res=await sess.execute(query)
            task_models=res.scalars().all()
            task_table=[TaskRead.model_validate(t) for t in task_models]
            return task_table
