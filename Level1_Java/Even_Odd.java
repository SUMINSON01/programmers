public class Even_Odd {
    public static String solution(int num) {
        String answer = (num%2) != 0 ? "Odd" : "Even";
        return answer;
    }

    public static void main(String[] args){
        int num;
        String answer;

        num = 3;
        answer = solution(num);
        System.out.println(answer);

        num = 4;
        answer = solution(num);
        System.out.println(answer);

    }
}
