export type Review = {
  id: string;
  createdBy: string;
  recipient: string;
  content: string;
  createdAt: string;       
  updatedAt: string;       
  deletedAt: string | null;  
  wasEdited: boolean;
};