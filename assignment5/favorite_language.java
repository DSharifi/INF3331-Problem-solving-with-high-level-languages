import java.util.*;
import java.util.stream.Collectors;

import java.io.*;



/*
Assume all tasks have least 1 or more in time for completion.
*/

class Project {
    Task[] tasks;
    int taskCount, latestTask;


    public Project(String path) {
        // create tasks
        initialize(path);

        // change int to Task (neighbour and dependency lists) for all Tasks
        
        for (Task task : tasks) {
            task.convertDependencies(this.tasks);
        }
    }

    private void initialize(String path) {
        try {
            File file = new File(path);
            Scanner in = new Scanner(file);

            // Tasks is defined as the first int token
            this.taskCount = in.nextInt();
            tasks = new Task[this.taskCount];

            int index = 0;
            while (in.hasNextLine()) {
                String tekst = in.nextLine();
                // empty line
                if (tekst.equals("")) {
                    continue;
                }
                String[] tekstArray = tekst.split("\\s+");

                // parse info to int
                int id = Integer.parseInt(tekstArray[0]);
                String name = tekstArray[1];
                int time = Integer.parseInt(tekstArray[2]);
                int manpower = Integer.parseInt(tekstArray[3]);

                // dependencies
                int[] dependencies = new int[tekstArray.length - 5];
                for (int i = 4, j = 0; i < tekstArray.length - 1; i++, j++) {
                    dependencies[j] = Integer.parseInt(tekstArray[i]);
                }
                // add Task
                this.tasks[index++] = new Task(id, name, time, manpower, dependencies);
            }
            in.close();

        } catch (Exception e) {
            System.out.println(e);
            System.exit(0);
        }
    }

    public void start() {
        cyclic();
        early();
        late();
        info();
        simulate();
    }

    private LinkedList<Task> readStartTasks(PriorityQueue<Task> startQueue) {
        LinkedList<Task> start = new LinkedList<Task>();
        Task task = startQueue.remove();        
        start.add(task);

        while(!startQueue.isEmpty() && (startQueue.peek().earlyStart == task.earlyStart)) {
            start.add(startQueue.remove());
        }

        return start;
    }

    private LinkedList<Task> readFinishTasks(PriorityQueue<Task> finishQueue) {
        LinkedList<Task> finish = new LinkedList<Task>();
        Task task = finishQueue.remove();
        finish.add(task);

        while (!finishQueue.isEmpty() && (finishQueue.peek().earlyFinish == task.earlyFinish)) {
            finish.add(finishQueue.remove());
        }

        return finish;

    }

    // simluates execution of the Project. All tasks are started and finished early.
    private void simulate() {

        int staff = 0;
        int time = 0;
        PriorityQueue<Task> startQueue = new PriorityQueue<Task>();
        PriorityQueue<Task> finishQueue = new PriorityQueue<Task>();
        
        for (Task task : tasks) {
            startQueue.add(task);
        }
        
        // while theres tasks to be completed



        while(!(startQueue.isEmpty() && finishQueue.isEmpty())) {

            LinkedList<Task> start = new LinkedList<Task>();
            LinkedList<Task> finish = new LinkedList<Task>();

            Task startTask = startQueue.peek();
            Task finishTask = finishQueue.peek();

            //startQueue er empty

            if (!startQueue.isEmpty() && (finishQueue.isEmpty() || (startTask.earlyStart < finishTask.earlyFinish))) {
                // only start values
                time = startTask.earlyStart;
                start = readStartTasks(startQueue);
                finishQueue.addAll(start);
            }
                
            else if (startQueue.isEmpty() || (startTask.earlyStart > finishTask.earlyFinish)) {
                // only finish values
                time = finishTask.earlyFinish;
                finish = readFinishTasks(finishQueue);
            }

            else {
                // both values
                time = finishTask.earlyFinish;
                start = readStartTasks(startQueue);
                finish = readFinishTasks(finishQueue);
                finishQueue.addAll(start);
            }

            for (Task newTask : start) {
                staff += newTask.manpower;
            }
            for (Task finishedTask : finish) {
                staff -= finishedTask.manpower;
            }
            printTime(start, finish, time, staff);
        }
        System.out.println("**** Shortest possible project execution is " + time + " ****");
    }

    // prints out each time frame
    private void printTime(LinkedList<Task> start, LinkedList<Task> finish, int time, int staff) {
        System.out.println("Time: " + time);
        for (Task finished : finish) {
            System.out.println("Finished: " + finished.id);
        }
        for (Task starting : start) {
            System.out.println("Starting " + starting.id);
        }
        System.out.println("Current staff: " + staff + "\n");
    }
    
    // prints out times
    private void info() {
        for (Task task : tasks) {
            String critical = "no";
            if (task.slack  == 0)
                critical = "yes";
            System.out.println("ID: " + task.id + ", --- " + task.name + " ---");
            System.out.println("Critical: " + critical + "\tManpower: " + task.manpower); 
            System.out.println("Slack: " + task.slack + "\tTime needed: " + task.time);
            System.out.println("Early Start " + task.earlyStart + "\tEarly Finish " + task.earlyFinish);
            System.out.println("Late Start " + task.lateStart + "\tLate Finish " + task.lateFinish);
            System.out.println("Tasks dependent (ID):");
            for (Task neighbour : task.neighbours) {
                System.out.println("\t"+neighbour.id);
            }
            System.out.println("\n\n");
        }
    }

    private void printLoop(ArrayList<Task> loop, Task task) {
        System.out.println("LOOP DETECTED!\n\n");
        String output = "";

        for (int i = 1; i < loop.size(); i++) {
            if (loop.get(i).status == 1){
                output += loop.get(i).name + " " + "(" + loop.get(i).id + ")" + " --> ";
            }
                    
        }
        output +=task.name + " " + "(" + task.id + ")";
        System.out.println(output);
    }

    private void dpsFindCyclic(Task task, ArrayList<Task> stack) {
        // stack for traversed tasks
        if (task.status == 1) {
            // loop found
            printLoop(stack, task);
            System.exit(0);

        } else if (task.status == 0) {
            // unseen task
            task.status = 1;
            stack.add(task);
            for (Task neighbour : task.neighbours) {
                dpsFindCyclic(neighbour, stack);
            }
            // task is done
            task.status = 2;
        }
    }

    // returns a Queue of all starting tasks
    private Queue<Task> findStartTasks() {
        return new LinkedList<>(Arrays.stream(tasks) // convert list to stream
                .filter(task -> task.dependencies.length == 0) // filter independent tasks
                .collect(Collectors.toList()));
    }


    // checks cycles by traversal of every starting task
    private void cyclic() {
        for (Task task : findStartTasks()) {
            if (task.status == 0) {
                dpsFindCyclic(task, new ArrayList<>());
            }
        }
    }



    private void early() {
        for (Task task : tasks) {
            earlyRecursive(task);
        }
    }

    // O(|V| + |E|)
    private void earlyRecursive(Task task) {
        // only calculate if not set
        if (task.earlyFinish == 0) {
            int maxTime = 0;
            // find latest early finish for dependencies
            for (Task dependency : task.dependencies) {
                // not calculated yet
                if (dependency.earlyFinish == 0) {
                    earlyRecursive(dependency);
                }
                // later finish
                if (maxTime < dependency.earlyFinish)
                    maxTime = dependency.earlyFinish;
            }
            // set times
            task.earlyStart = maxTime;
            task.earlyFinish = maxTime + task.time;

            if (task.earlyFinish > latestTask) {
                latestTask = task.earlyFinish;
            }
        }
    }

    private void late() {
        for (Task task : tasks) {
            lateRecursive(task);
        }
    }

    // sets late starts, and determines slack
    private void lateRecursive(Task task) {
        
        // only run if late is not set
        if (task.lateFinish == 0) {

            // finishing task
            if (task.neighbours.isEmpty()) {
                task.lateFinish = latestTask;
                task.slack = task.lateFinish - task.earlyFinish;
                task.lateStart = task.earlyStart - task.slack;
            }

            int minTime = latestTask;

            // find earliest late start of neighbours
            for (Task neighbour : task.neighbours) {
                if (neighbour.lateStart == 0) {
                    lateRecursive(neighbour);
                }
                if (minTime > neighbour.lateStart) {
                    minTime = neighbour.lateStart;
                }
            }
            // set late times
            task.lateFinish = minTime;
            task.lateStart = task.lateFinish - task.time;

            // set slack
            task.slack = task.lateFinish - task.earlyFinish;
        }
    }

}
