/**
 * Interface for the Letter object.
 * @interface
 * @property {string} letter - The letter in the Letter object.
 * @property {("NORMAL"|"CLUE"|"GOOD"|"BAD")} type - The type of the letter. It can be "NORMAL", "CLUE", "GOOD", or "BAD".
 */
export interface Letter {
    letter: string;
    type: "NORMAL" | "CLUE" | "GOOD" | "BAD"
}