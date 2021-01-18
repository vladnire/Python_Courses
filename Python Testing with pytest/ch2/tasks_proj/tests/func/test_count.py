"""Test the tasks.count() API function."""

import pytest
import tasks
from tasks import Task


def test_count_first():
    """tasks.count() should return empty at database init."""
    tasks_nr = tasks.count()
    assert tasks_nr == 0
    
    
def test_count_multiple():
    """Test after adding three tasks."""
    for e in ['do something', 'do nothing', 'do else']:   
        new_task = Task(e)   
        tasks.add(new_task)
    tasks_nr = tasks.count()
    assert tasks_nr == 3   
    

def test_count_remove():
    """Test after removing a task."""
    for e in ['do something', 'do nothing', 'do else']:   
        new_task = Task(e)   
        tasks.add(new_task)
    tasks.delete(3)
    tasks_nr = tasks.count()
    assert tasks_nr == 2   
    
    
def test_count_empty():
    """Test county afeter emptying the database"""
    for e in ['do something', 'do nothing', 'do else']:   
        new_task = Task(e)   
        tasks.add(new_task)
    tasks.delete_all()
    tasks_nr = tasks.count()
    assert tasks_nr == 0  
    

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()
