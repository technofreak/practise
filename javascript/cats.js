/**
 * Created by Parthan on 10/21/13.
 *
 * Based on Chapter 4 of Eloquent Javascript
 *
 * Aunt Emily emails us about her cats every time she mails us. We want to record them and have a list of living cats at
 * any point in time. Also, she mentions the genealogy of her cats in her mails.
 *
 * Example:
 * born 21/04/2006 (mother Lady Gaga): Red Lion, Brave Jone
 * died 09/05/2006: General Hobbes
 *
 * Execution Plan:
 * 1. Go over the email archive, in chronological order
 * 2. Read the mail parah by parah, to start with 'born' or 'died'
 * 3. Add names of born cates to the list of living cats
 * 4. Remove the names of dead cats from the list of living cats
 */

var sample_text = "";

