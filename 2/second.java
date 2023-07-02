import java.util.*;

public class MAin {

    public static void main(String[] args) {
        //1 | prec | C_max
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int e = scanner.nextInt();

        int[] times = new int[n+1];
        @SuppressWarnings("unchecked")
        ArrayList<Integer>[] graph =  new ArrayList[n+1];

        for (int i = 1; i <= n; i++) {
            times[i] = scanner.nextInt();
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < e; i++) {
            int k = scanner.nextInt();
            int l = scanner.nextInt();
            graph[k].add(l);
        }

        int[] indegree = new int[n+1];
        for (int i = 1; i <= n; i++) {
            for (int v : graph[i]) {
                indegree[v]++;
            }
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 1; i <= n; i++) {
            if (indegree[i] == 0) {
                pq.offer(i);
            }
        }

        List<Integer> order = new ArrayList<>();

        while (!pq.isEmpty()) {
            int u = pq.poll();
            order.add(u);

            for (int v : graph[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    pq.offer(v);
                }
            }
        }

        int totalTime = 0;
        for (int i : order) {
            totalTime += times[i];
        }

        //printujemy wyjscie
        for (int i : order) {
            System.out.println(i);
        }
        System.out.println(totalTime);
    }
}