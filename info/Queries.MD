Нужно получить все вопросы из этого опроса, на которые юзер уже ответил

ORM (confirmed)
answered = Question.objects.filter(answers__user='1',poll = poll_id )

SQL (not confirmed)
FROM Questions q select *
	Join Polls on q.poll_id = poll.id
Where q.id not in(
	select answerd.id
	From answers
	where user == user.id)
where p.id = 1

