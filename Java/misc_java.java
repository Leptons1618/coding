
/* Quine */
// class S{public static void main(String[]a){String p="class S{public static void main(String[]a){String p=%c%s%1$c;System.out.printf(p,34,p);}}";System.out.printf(p,34,p);}}

/* Simple Addition */
class sum_cla 
{
    public static void main(String[] lol) 
    {
        int sum = 0;
        for (int i = 0; i < lol.length; i++) {
            sum += Integer.parseInt(lol[i]);
        }
        System.out.println(sum);
    }
}

/* Check Vowel Or Consonent */
// class chkVorC
// {
// static String check(char args)
// {
//     if(Character.getType(args) == 1 || Character.getType(args) == 2)
//     {
//         switch(args)
//         {
//             case 'a','A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U':
//             return "vowel";
//             default:
//             return "consonent";
//         }
//     }else
//         return "Not an alphabet.";
// }
// public static void main(String[] inp) {
//     char ch = inp[0].charAt(0);
//     System.out.println(check(ch));
// }
// }

/* Check typeof */
// class typeof{
//     public static void main(String[] args) {
//         char ch = args[0].charAt(0);
//         System.out.println(Character.getType(ch));
//     }
// }



