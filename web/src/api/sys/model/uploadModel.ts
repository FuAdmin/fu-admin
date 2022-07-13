export interface UploadApiResult {
  message: string;
  code: number;
  result: {
    url: string;
    name: string;
  };
}
