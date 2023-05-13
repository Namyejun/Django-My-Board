from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")

    writer = models.ForeignKey(to='user.User', on_delete=models.CASCADE, verbose_name="작성자")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성시간")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = "tb_board"