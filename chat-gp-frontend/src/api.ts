
export type CategoryResponse = {
  model: string;
  pk: number;
  fields: {
    name: string;
    image: string;
    description: string;
  }
}

export async function getAllCategories() {
  const response = await fetch("http://localhost:8000/chat-gp/category/all");
  const data = await response.json();

  if (!response.ok) {
    throw new Error("FUCK")
  }

  return data as CategoryResponse[];
}

export type ForumData = {
  model: string;
  pk: number;
  fields: {
    category: number;
    image: string;
    name: string;
    description: string;
  }
}

export type ForumResponse = { ok: false } | {
  ok: true;
  forums: ForumData[]
}

export async function getAllForums(category: string): Promise<ForumResponse> {
  const response = await fetch(`http://localhost:8000/chat-gp/${category}/forums`);
  const data: ForumData[] = await response.json();

  if (!response.ok) {
    return { ok: false }
  }

  return { ok: true, forums: data };
}


export async function getForumByName(category: string, forum: string): Promise<ForumResponse> {
  const response = await fetch(`http://localhost:8000/chat-gp/${category}/${forum}`);
  const data: ForumData[] = await response.json();

  if (!response.ok) {
    return { ok: false }
  }

  return { ok: true, forums: data };
}

export type MessageData = {
  model: string;
  pk: number;
  fields: {
    user: number;
    forum: number;
    content: string;
    time_stamp: string;
  }
}

export type MessageResponse = { ok: false } | {
  ok: true;
  messages: MessageData[]
}


export async function getAllMessages(category: string, forum: string): Promise<MessageResponse> {
  const response = await fetch(`http://localhost:8000/chat-gp/${category}/${forum}/messages`);
  const data: MessageData[] = await response.json();

  if (!response.ok) {
    return { ok: false }
  }

  return { ok: true, messages: data };
}


export type PostData = {
  model: string;
  pk: number;
  fields: {
    user: number;
    forum: number;
    title: string;
    content: string;
    time_stamp: string;
  }
}

export type PostResponse = { ok: false } | {
  ok: true;
  posts: PostData[]
}


export async function getAllPosts(category: string, forum: string): Promise<PostResponse> {
  const response = await fetch(`http://localhost:8000/chat-gp/${category}/${forum}/posts`);
  const data: PostData[] = await response.json();

  if (!response.ok) {
    return { ok: false }
  }

  return { ok: true, posts: data };
}
