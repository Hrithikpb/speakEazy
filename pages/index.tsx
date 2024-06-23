import {
  BookOpenText as BookIcon,
  Ear as EarIcon,
  Microphone as MicrophoneIcon,
  SmileySticker as SmileyIcon,
} from "@phosphor-icons/react";

import Link from "next/link";

export default function HomePage() {
  return (
    <div className="px-6 py-10 pb-20 sm:px-10 md:px-14">
      <div className="text-center md:text-left">
        <div className="text-center pb-2 text-4xl font-medium text-neutral-700">SpeakEazy</div>
        <div className="text-center pt-5">Select your choice for today.</div>

        <div className="md:px-10 flex flex-col pt-12 grid-cols-1 md:grid-cols-2 gap-4">
          <ModelSection name="Record with web cam" page="/face" iconClass={SmileyIcon} />
          <ModelSection name="Record with mic only" page="/burst" iconClass={MicrophoneIcon} />
        </div>
      </div>
    </div>
  );
}

type ModelSectionProps = {
  iconClass: any;
  name: string;
  page: string;
};

function ModelSection(props: ModelSectionProps) {
  return (
    <Link href={props.page}>
      <div className="hover:border-neutral-400 hover:ease-linear duration-200 flex w-full justify-center items-center rounded-lg border border-neutral-200 bg-white px-14 py-12 shadow">
        <props.iconClass size={40} />
        <div className="ml-6 text-xl">{props.name}</div>
      </div>
    </Link>
  );
}
