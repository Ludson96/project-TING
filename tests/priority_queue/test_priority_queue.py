from ting_file_management.priority_queue import PriorityQueue
from tests.priority_queue.mock_data import alta_prioridade, baixa_prioridade
import pytest


def test_basic_priority_queueing():
    priority = PriorityQueue()

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority.search(3)

    priority.enqueue(baixa_prioridade)
    assert len(priority.regular_priority) == 1

    priority.enqueue(alta_prioridade)
    assert len(priority.high_priority) == 1
    assert len(priority) == 2

    assert priority.search(0) == alta_prioridade
    assert priority.search(1) == baixa_prioridade

    item_removido = priority.dequeue()
    assert item_removido == alta_prioridade
    assert len(priority.regular_priority) == 1
    assert len(priority.high_priority) == 0
    assert len(priority) == 1
