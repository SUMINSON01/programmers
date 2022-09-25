public class divisior_sum {
    public static int solution(int n) {
        int answer = 0;
        int i = 1;

        while(i <= n) {
            if(n % i == 0)
                answer += i;
            i++;
        }

        return answer;
    }

    public static void main(String[] args){
        int n;
        int answer;

        n = 28;
        answer = solution(n);
        System.out.println(answer);

    }
}
