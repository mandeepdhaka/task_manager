import time


def lambda_simulation(task_status):
    """_summary_

    Use to simulate notification sending
    """
    if task_status == 'completed':
        
        print("Simulating Lambda: Task completed!")
        
        time.sleep(1)  # Simulate time for Lambda processing
    else:
        print("Task not completed yet.")


lambda_simulation('completed')
